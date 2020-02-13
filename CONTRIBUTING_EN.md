# Guide For contribution <!-- omit in toc -->

- [To submit data](#to-submit-data)
- [To submit a new issue or initialize a pull request](#to-submit-a-new-issue-or-initialize-a-pull-request)
  - [0、To submit a new issue](#0to-submit-a-new-issue)
  - [1、To claim task](#1to-claim-task)
  - [2、To fork this repository](#2to-fork-this-repository)
  - [3、Clone the repository](#3clone-the-repository)
  - [4、To create a `branch`](#4to-create-a-branch)
  - [5、To modify content and submit](#5to-modify-content-and-submit)
  - [6、Upstream repository change synchronization](#6upstream-repository-change-synchronization)
  - [7、To push new branch to remote repository](#7to-push-new-branch-to-remote-repository)
  - [8、To create a `Pull Request`](#8to-create-a-pull-request)
  - [9、To resolve a merge conflict](#9to-resolve-a-merge-conflict)
  - [10、After the merge, you can：](#10after-the-merge-you-can)
- [Robot specification](#robot-specification)
- [Meet us on Slack](#meet-us-on-slack)

## To submit data

**This is the main repository, all the data import is accomplished automatically by scripts. So please don’t submit data to this repository directly. To submit data , please check [README](./README.md)**。

> This platform uses Shimo (a cloud-based productivity suite) to collect data. The data will be automatically submitted to the repository in the form of Rps by scripts.

> Since there are lots of contributors, we won’t give everyone the authority
to edit, please fill in a form of application [here](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill). We will invite you to input information to certain sheets or forms.

## To submit a new issue or initialize a pull request
In this guide we will try describing how to submit a new issue or initialize a pull request as detailed as we can. Welcome to contribute to **wuhan2020** !

### 0、To submit a new issue

If you have any good ideas, click [here](https://github.com/wuhan2020/wuhan2020/issues) to submit a new `issue`，our volunteers will discuss it with you in time.

When submitting a new `issue`， please pay attention to the type of the `issue` and explain it in the headline. The issue will be tagged automatically：

-   hospital: information relating to hospitals
-   factory: information relating to manufacturing and production
-   logistical: logistical information
-   hotel: information relating to hotels
-   donation：information relating to donation
-   clinic：information relating to voluntary clinic
-   news：news update on this Covid-19 epidemic prevention
-   doc: about documentation
-   bug： bug report
-   feature: new features

### 1、To claim task

> **Let’s work together through this tough period to fight against the coronavirus !!**

Select a task from the [Issue List](https://github.com/wuhan2020/wuhan2020/issues). and then claim it by using `/self-assign`. The robot of the project will set `Assignees` of the `issue` to yourself automatically.

```
/self-assign
```

Shown as the following：

![self-assign 示意图](./static/self-assign.png)

### 2、To fork this repository

Visit [wuhan2020](https://github.com/wuhan2020/wuhan2020). And then fort it to your own account.

![Fork 仓库](./static/fork-repo.png)

> Nota Bene :  the following commands are supposed to be done in console, [Git](https://git-scm.com/) is needed.

### 3、Clone the repository

Back to your won GitHub page，find the _wuhan2020_ that you just forked，enter it, `clone` it to local, like :

```bash
# replace the XXX with your own user name
git clone git@github.com:XXX/wuhan2020.git
cd wuhan2020
```

### 4、To create a `branch`

> It’s not recommended to develop in the master branch unless the urgent recovery.

According to the purpose, create a new branch and appropriately name it, run like this :

```bash
git checkout -b my-fix-branch master
```

### 5、To modify content and submit

Modify the corresponding file and submit :

```bash
git add .
git commit -m "hotel: update HOTEL.csv, fix #1"
```

Pay attention to :

(1) clarify in one sentence for what have been done

(2) relate the `issue`，for example `fix #1` 、`close #2`、`#3`

If there is modification after `commit` , use the parameter `--amend`：

```bash
git add .
git commit --amend -sm "hotel: update HOTEL.csv, fix #1"
```

### 6、Upstream repository change synchronization

To avoid upstream repository change synchronization ([wuhan2020/wuhan2020](https://github.com/wuhan2020/wuhan2020) )，it’s necessary to sync your local repository with the upstream：

```bash
$ git remote add upstream git@github.com:wuhan2020/wuhan2020.git
$ git fetch upstream
```

If there have been changes to the upstream repo already, please run `rebase` at first :

```bash
$ git rebase upstream/master
```

### 7、To push new branch to remote repository

```bash
$ git push -f origin my-fix-branch:my-fix-branch
```

### 8、To create a `Pull Request`

Create a `pull request` to the upstream repository. As shown:

![pull-request](./static/pull-request.png)

![open-pr](./static/open-pr.png)
如果其他人 `review` 之后，需要再进行更改，就修改相关内容，然后执行以下操作，该 PR 将会自动同步该 `commit` 。

```bash
git add .
git commit --amend
git push -f origin my-fix-branch
```

### 9、To resolve a merge conflict

> Nota bene : if no conflict occurs, no need to do these

-   Sync with upstream repo

```bash
git fetch upstream
```

-   Run `rebase`:

```bash
git rebase upstream/master
```

-   Manually resolve the conflict, then submit

```bash
git add my-fix-file
git rebase --continue
git push -f origin my-fix-branch
```

### 10、After the merge, you can：

-   Switch back to `master`：

```bash
git checkout master -f
```

-   Keep the `master` in sync with the upstream branch：

```bash
git pull --ff upstream master
```

-   Delete local branch (optional):

```bash
git branch -D my-fix-branch
```

-   Delete remote branch (optional)：

```bash
git push origin --delete my-fix-branch
```

## Robot specification

This project has been granted access to GitHub robot :`Menbotics`，it can：

-   **Tag `Issue` automatically**：Please check [0、To submit a new issue](#0To submit a new issue) for more details
-   **To claim task**：Please check [1、To claim task](#1To claim task)
-   **Merge automatically**：When a PR(Pull Request) is submitted，the ones who have the authority will use `/approve`  to merge automatically.

To know details of robot configuration, please check [hypertrons.json](./.github/hypertrons.json)，for example, to see who have the merging authority.

## Meet us on Slack

Furthermore , we have our [Slack group](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)，where those channels for frontend backend and data sync are already prepared , meet us on Slack for a better communication both on technical and non-technical themes.
Let's work together through this tough period to fight against the coronavirus!
