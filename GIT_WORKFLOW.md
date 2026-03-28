# Git Workflow for `Projects` Repo

A one-page guide to pull, add work, and push without errors.

## Daily flow
1. Open terminal and go to repo root:
   ```powershell
   cd "C:\Users\Fares\Desktop\python\Projects"
   ```
2. Pull latest before you start:
   ```powershell
   git pull origin main
   ```
3. Do your work (edit files, add new folders, etc.).
4. Stage, commit, push when done:
   ```powershell
   git add .
   git commit -m "<what you changed>"
   git push origin main
   ```

## Add a new project (example path)
1. Make the folder under the correct parent, e.g. for freeCodeCamp data analysis:
   ```powershell
   mkdir "FreeCodeCamp\Data_Analysis\your-project-name"
   ```
2. Put files inside that folder.
3. From repo root, stage/commit/push:
   ```powershell
   git add .
   git commit -m "Add your-project-name"
   git push origin main
   ```

## Update an existing project
1. Start at repo root and pull latest:
   ```powershell
   git pull origin main
   ```
2. Edit files.
3. Stage/commit/push (same as above).

## Golden rules
- Always `git pull` before starting work.
- Run git commands from the repo root (`C:\Users\Fares\Desktop\python\Projects`).
- Use clear commit messages.
- Avoid pushing from inside a nested clone or boilerplate folder.

## Handling conflicts (quick)
If `git pull` shows conflicts:
1. Open conflicted files, choose the correct content, remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
2. Mark resolved and continue:
   ```powershell
   git add .
   git commit -m "Resolve merge conflicts"
   git push origin main
   ```

## Quick status checks
- What changed?
  ```powershell
  git status
  ```
- Last commits log:
  ```powershell
  git log --oneline -5
  ```

Happy coding! 🚀
