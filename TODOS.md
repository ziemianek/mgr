## TODO List
1. **Fix this issue:**

    ```bash
    (.taskmgr) ➜  mgr git:(test/testagain) ✗ git commit -m "idk"
    Auto packing the repository in background for optimum performance.
    See "git help gc" for manual housekeeping.
    warning: The last gc run reported the following. Please correct the root cause
    and remove .git/gc.log
    Automatic cleanup will not be performed until the file is removed.

    warning: There are too many unreachable loose objects; run 'git prune' to remove them.

    [test/testagain 1e7d666] idk
     2 files changed, 2 insertions(+), 1 deletion(-)
    ```

Fix: https://stackoverflow.com/questions/35738680/avoiding-warning-there-are-too-many-unreachable-loose-objects-during-git-svn
``` bash
    (.taskmgr) ➜  mgr git:(test/testagain) cat .git/gc.log             
    warning: There are too many unreachable loose objects; run 'git prune' to remove them.
    (.taskmgr) ➜  mgr git:(test/testagain) ✗ git help gc

    (.taskmgr) ➜  mgr git:(test/testagain) ✗ git help push
    (.taskmgr) ➜  mgr git:(test/testagain) ✗ git gc --aggressive
    Enumerating objects: 350, done.
    Counting objects: 100% (350/350), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (292/292), done.
    Writing objects: 100% (350/350), done.
    Total 350 (delta 117), reused 232 (delta 0), pack-reused 0
    (.taskmgr) ➜  mgr git:(test/testagain) ✗ rm .git/gc.log
    rm: .git/gc.log: No such file or directory
```
2. **Learn how to properly architect Kubernetes cluster for microservices app**

3. **Learn how to architect infra for the project**
