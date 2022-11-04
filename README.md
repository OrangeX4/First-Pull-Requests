# Level 2: Advance in Upstream when PR

我们把`OrangeX4/First-Pull-Requests`叫做“上游分支”，当你执行fork操作后，你的github中会产生一个名为`你的名字/First-Pull-Requests`的仓库。

现在我们假设这样一种情况：敏锐的你修正了代码中的一个小Bug，并且把修复Bug的代码推送到了属于你的仓库中。现在你希望上游分支（`OrangeX4/First-Pull-Requests`）也能修复这个Bug，便向它发送了你的第二个PR。

——但是不巧的是，上游分支在你fork之后也做了许多改动，提交了一些新的commit，也就是说，上游分支的代码与你的代码分道扬镳了！`OrangeX4`希望你能够把上游分支的代码中的新改动一起合并到你的代码中，并提交一个新的PR。

具体而言，你需要
+ 在底下的评论区留下你的评论，形式为
  ```markdown
  ### 你的名字
  
  想说的话
  ```
+ 检查上游分支的代码，查看上游分支的存在超前的commit
+ 使用`git fetch`命令，获取上游分支的版本信息
+ 使用`git merge / git rebase`，将上游分支的代码改动合并到本地
+ 将合并后的改动提交到`你的用户名/First-Pull-Requests`
+ 向`OrangeX4`发出PR

在这个实验中，`git merge`和`git rebase`一定不会出现冲突。我们将在level3中处理这种更加复杂的情况

## 评论区

### typoverflow

测试一下这个新功能ORZ

### vocaltract

新测试

### haha

大家好

<!-- 在上面的评论区留言，不要修改下面的代码 -->

---
当前最新的一次fork的时间戳为：
<!-- BEGIN:TAG -->
Fri Nov  4 00:39:13 UTC 2022
<!-- END:TAG -->
---
