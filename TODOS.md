1. **Fix this issue:**
```bash

(.taskmgr) ➜ mgr git:(test/testagain) ✗ git commit -m "idk"

Auto packing the repository in background for optimum performance.

See "git help gc" for manual housekeeping.

warning: The last gc run reported the following. Please correct the root cause

and remove .git/gc.log

Automatic cleanup will not be performed until the file is removed.

  

warning: There are too many unreachable loose objects; run 'git prune' to remove them.

  

[test/testagain 1e7d666] idk

2 files changed, 2 insertions(+), 1 deletion(-)

```

Fix
``` bash

(.taskmgr) ➜ mgr git:(test/testagain) cat .git/gc.log

warning: There are too many unreachable loose objects; run 'git prune' to remove them.

(.taskmgr) ➜ mgr git:(test/testagain) ✗ git help gc

  

(.taskmgr) ➜ mgr git:(test/testagain) ✗ git help push

(.taskmgr) ➜ mgr git:(test/testagain) ✗ git gc --aggressive

Enumerating objects: 350, done.

Counting objects: 100% (350/350), done.

Delta compression using up to 8 threads

Compressing objects: 100% (292/292), done.

Writing objects: 100% (350/350), done.

Total 350 (delta 117), reused 232 (delta 0), pack-reused 0

(.taskmgr) ➜ mgr git:(test/testagain) ✗ rm .git/gc.log

rm: .git/gc.log: No such file or directory

```

I still see this ....
``` bash
(.taskmgr) ➜ mgr git:(test/testagain) ✗ git commit -m "idk"

Auto packing the repository in background for optimum performance.

See "git help gc" for manual housekeeping.

[test/testagain 2e4ae52] idk

4 files changed, 35 insertions(+), 175 deletions(-)

delete mode 100644 TODOS_v1.md

delete mode 100644 TODOS_v2.md

delete mode 100644 roadmap.md
```

  I used `git fsck` and look at this. I ve seen a handful of those lol:
```
dangling blob f5bfed6fef4cdbea96e8d76b561e3402e0347eca
dangling blob f8ff4349e1fd9a5e67a98b02e2d45c9c045cf3af
dangling blob feffa194e077abdc73429f6206e125f84742524a
dangling blob ffbff011367d6858f3bb5e8b07f7f2b0459aaf2b
Verifying commits in commit graph: 100% (48/48), done.  
```
  Then this
  ``` bash
(.taskmgr) ➜  mgr git:(test/testagain) ✗ git gc --prune=now

Enumerating objects: 353, done.
Counting objects: 100% (353/353), done.
Delta compression using up to 8 threads
Compressing objects: 100% (178/178), done.
Writing objects: 100% (353/353), done.
Total 353 (delta 118), reused 352 (delta 117), pack-reused 0
```

DONE:
``` bash
(.taskmgr) ➜  mgr git:(test/testagain) ✗ git commit -m "idk"
On branch test/testagain
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   TODOS.md

no changes added to commit (use "git add" and/or "git commit -a")
(.taskmgr) ➜  mgr git:(test/testagain) ✗ git add -A         
(.taskmgr) ➜  mgr git:(test/testagain) ✗ git commit -m "idk"
[test/testagain 30f9205] idk
 1 file changed, 12 insertions(+)
(.taskmgr) ➜  mgr git:(test/testagain) git push -u origin test/testagain
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 8 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (10/10), 1.59 KiB | 1.59 MiB/s, done.
Total 10 (delta 5), reused 4 (delta 1), pack-reused 0
remote: Resolving deltas: 100% (5/5), completed with 2 local objects.
remote: 
remote: Create a pull request for 'test/testagain' on GitHub by visiting:
remote:      https://github.com/ziemianek/mgr/pull/new/test/testagain
remote: 
To github.com:ziemianek/mgr.git
 * [new branch]      test/testagain -> test/testagain
branch 'test/testagain' set up to track 'origin/test/testagain'.
(.taskmgr) ➜  mgr git:(test/testagain)                                  
```


2. **Learn how to properly architect Kubernetes cluster for microservices app**

chat gpt gave bunch of resources for me to check out:
### **Kubernetes & Microservices**  
- [A Cloud Architect’s Guide to Kubernetes & Microservices](https://deploy.equinix.com/blog/a-cloud-architects-guide-to-kubernetes-microservices/)  
- [Spring Boot & Kubernetes Guide](https://learnk8s.io/spring-boot-kubernetes-guide)  
- [Using Kubernetes for Microservices](https://www.loft.sh/blog/a-guide-to-using-kubernetes-for-microservices)  
- [Microservices vs. Monolith (Atlassian)](https://www.atlassian.com/microservices/microservices-architecture/microservices-vs-monolith)  
- [Google Cloud: What is Microservices Architecture?](https://cloud.google.com/learn/what-is-microservices-architecture?hl=en)  
- [Kubernetes & Microservices Guide (Last9)](https://last9.io/blog/kubernetes-microservices/)  
- [Deploying a RESTful API Using Kubernetes](https://medium.com/@saifullahshah818/deploying-a-restful-api-using-kubernetes-9a47b85ea62a)  
- [Kubernetes API Concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)  
- [Thesis on Microservices Architecture](https://www.theseus.fi/bitstream/handle/10024/356037/Hampf_Kare.pdf)  
- [Structuring Backend REST API with Kubernetes](https://stackoverflow.com/questions/51664038/structuring-backend-rest-api-into-microservices-with-kubernetes-or-serverless)  
- [Kubernetes & Microservices Overview](https://www.youtube.com/watch?v=XuSQU5Grv1g)  
- [Google Cloud Microservices Architecture](https://www.youtube.com/watch?t=1465s&v=j6ow-UemzBc)  
- [Kubernetes in 5 Minutes](https://www.youtube.com/watch?v=1xo-0gCVhTU)  

3. **and how to deploy it**

same, got it from chatgpt:
### **Task Management & Web Apps**  
- [Task Management Web App Template](https://uizard.io/templates/web-app-templates/task-management-web-app/)  

### **AWS & Cloud Architecture**  
- [AWS Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=*all)  
- [AWS Architecture Center](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all)  
- [AWS TV Video](https://aws.amazon.com/ar/awstv/watch/5ff9f227de2/)  
- [AWS Solution Architect Associate Projects](https://www.theknowledgeacademy.com/blog/aws-solution-architect-associate-projects/)  
- [AWS Hands-On Video](https://www.youtube.com/watch?v=5gnoVjpfWxU)  

4. remember - for tasks 2 and 3 try to make notes, they may be useful for theoretical part of the project

5. setup kanban board for easier tasks management (github projects)

---
### Źródła:
- fix to 1st task https://stackoverflow.com/questions/35738680/avoiding-warning-there-are-too-many-unreachable-loose-objects-during-git-svn
