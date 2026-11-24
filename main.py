"""Entrypoint that writes the required statement to the output directory."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
import pathlib

LINE = "I am not dying from exhaustion, I am committing assisted suicide after three years of having to render your atrocious ex-boyfriend's selfies in 4K."

def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content length or whitespace-only.")
    
    out_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = pathlib.Path(out_dir_str)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = out_dir / "entry.txt"
    target_path.write_text(content, encoding="utf-8")
    
    if out_dir_str != "/output":
        try:
            default_dir = pathlib.Path("/output")
            default_dir.mkdir(parents=True, exist_ok=True)
            (default_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass
            
    print(str(target_path))
    print(len(content))

if __name__ == "__main__":
    main()
