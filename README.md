# Veckouppgift 4  Git, CI & CD
By Araceli Jakobsson



## 1 Discussions
1 What benefits can you see with CI & CD in your workplace?
Those of you who are not working: how would you like it to work in your future workplace?
* Not currently working, CI & CD are ideal as it can bring automated pipelines, a strong test culture, with unit tests, integration tests, and performance tests in every additional code added or developed over time. This also enables quick deployment, transparency and visibility, safe deployment practices, and a continuous improvement mindset.

2 What is the point of linting?
* Linting can catch errors early, it can enforce consistent style, improve code quality, save time in code reviews and integrate with CI/CD.

3 How do you work with git and multiple branches within a team?
<br /> Working with Git in a team by:
* Get the latest code using git pull from origin main
* Create a branch for the assigned task
* Write code locally and commit
* Once done, push to origin feature
* Open a pull request from own branch with all the details about what has been done
* CI/CD to test, linting, and verify
* Do code review with teammates, make changes if needed
* Update and push to the same branch
* Merge into main to make it part of the main project
* Delete local branch

4 What is a pull request?
* A pull request (PR) is a way to propose your code changes to a team and ask for them to be reviewed and merged into the main code.


## 2 Project
Workflow
```
testverktyg_04_CI_CD/
├─ README.md
├─ .gitignore
├─ requirements.txt
├─ pytest.ini
├─ setup.cfg
├─ .github/
|  └─ workflows/
|     └─ python-ci.yml
├─ src/
|  └─ algorithms/
|     └─ bubble_sort.py
├─ tests/
|  └─ integration/
|     └─ test_bubble_sort_integration.py
|  └─ unit/
|     └─ test_bubble_sort_unit.py
```

Unit Test
```commandline
pytest -v -m unit
```

Integration test
```commandline
pytest -v -m integration
```
