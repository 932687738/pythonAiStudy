# AI Study Python Implementations

This project implements the course examples from:

`D:\cache\workspace\test\study\chapters`

The code is organized by chapter under `ai_study/chapters`. Each module exposes:

- `TITLE`
- chapter-specific helper functions
- `run()`, which returns a small runnable demo result
- a standalone script entry, so each chapter can be run by itself

## Usage

List all standalone chapter commands:

```powershell
python main.py
```

Run a chapter directly:

```powershell
python -m ai_study.chapters.machine_learning_workflow
```

Other examples:

```powershell
python -m ai_study.chapters.ai_overview
python -m ai_study.chapters.supervised_learning
python -m ai_study.chapters.advanced_moe
```

The examples intentionally use the Python standard library only. This keeps the project runnable even before installing packages such as NumPy, pandas, scikit-learn, or PyTorch. The Spring AI and LangChain4j chapters are represented as Python-side engineering pattern mappings because their original course material is Java-focused.
