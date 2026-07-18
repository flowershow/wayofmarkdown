# Github FAQs and Tips

### FAQ: When do I need to create a new branch vs committing directly to main?

Creating a new branch allows you to work on your changes without affecting the ‘main’ branch, which is the primary copy of the project - the one which is used to build the live version of the website. This way, the main project remains undisturbed until your changes are reviewed, approved and merged to the main branch (copy) of the repository.

### Tip: How to name your branches.

When naming a GitHub branch, keep it concise and descriptive. Use hyphens or underscores to separate words, and include relevant context like the feature, bug, or issue number you’re working on.

### Tip: How to write a good commit message (and a description).

Your commit message should be no longer than 50 chracters. It should be a concise explanation of your changes - a phrase, rather than a full sentence(s). It shouldn’t end with a dot and should use imperative, present tense, e.g. “Fix typo in xyz.md”. You can add more information in the description field, which should be no longer than 72 characters.

### FAQ: What does “commit changes” mean?

Committing changes is like saving a file. In the context of GitHub, it means you’re saving your edits or additions to the repository - or strictly, to a given branch of the repository. Each commit is accompanied by a message describing the changes, which makes it easy to track modifications over time.

### FAQ: What is a branch?

A branch is a copy of the main project codebase. When you create a new branch, you are essentially creating a copy of the project codebase that you can work on without affecting the main project codebase.

### FAQ: What is a Pull Request?

A Pull Request is a request to merge changes from one branch into another, usually the main branch.

### FAQ: How do I do a Pull Request?

If you have created a branch, instead of submitting directly to the main branch, after clicking “Propose changes”, you’ll then be redirected to the “Open a pull request” page, where you’ll see a summary of your modifications.

Review your Pull Request to ensure all the changes are as intended. If needed, provide additional context or explanation in the comment box.

When everything is in order, you can click “Create Pull Request”.

Once your Pull Request has been created, it will be reviewed by the project team. If the project team approves your Pull Request, it will be merged into the main project branch, and after that, it should be live on the website.
