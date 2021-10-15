# Python HackerRank Solutions

[My HackerRank Profile](https://www.hackerrank.com/dwarnold)

The `src` directory contains a hierarchy of Python solutions for different HackerRank problems.

The `tests` directory contains a hierarchy of unit test classes, with each unit test class corresponding to a specific
HackerRank problem.

### Run all Unit Tests

```shell
python -m unittest discover -s <PATH_TO_REPO>/python-hackerrank/tests
```

### Add Git Hooks

See `pre-push` shell script in `hooks/`. When pushing to the `main` branch, a push is only successful when all unit
tests pass.

To utilise this `pre-push` git hook, run the following commands in the project root directory:

```shell
# Copy all repo git hooks, into the `.git/hooks/` dir.
cp -av hooks/* .git/hooks

# Set all git hooks to executable, if not already set.
chmod +x .git/hooks/*
```

### Generate Python packages for both `src` and `tests` directories

In `main.py`, see `generate_packages()` function.

Can be run with `main()` method:

```shell
python main.py --sep "/" --path InterviewPreparationKit/Miscellaneous
python main.py --sep "." --path InterviewPreparationKit.Miscellaneous
```

Result (Will create each if they each do not already exist):

```text
src/InterviewPreparationKit/
src/InterviewPreparationKit/__init__.py
src/InterviewPreparationKit/Miscellaneous/
src/InterviewPreparationKit/Miscellaneous/__init__.py
tests/InterviewPreparationKit/
tests/InterviewPreparationKit/__init__.py
tests/InterviewPreparationKit/Miscellaneous/
tests/InterviewPreparationKit/Miscellaneous/__init__.py
```
