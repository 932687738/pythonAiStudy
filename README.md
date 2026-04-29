# AI Study Python Implementations

This project implements the course examples from:

`D:\cache\workspace\test\study\chapters`

The code is organized by chapter under `ai_study/chapters`. Each module exposes:

- `TITLE`
- chapter-specific helper functions
- `run()`, which returns a small runnable demo result

## Usage

List all chapters:

```powershell
python main.py --list
```

Run one chapter:

```powershell
python main.py 03
```

The examples intentionally use the Python standard library only. This keeps the project runnable even before installing packages such as NumPy, pandas, scikit-learn, or PyTorch. The Spring AI and LangChain4j chapters are represented as Python-side engineering pattern mappings because their original course material is Java-focused.
