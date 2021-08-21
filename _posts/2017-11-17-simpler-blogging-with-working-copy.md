---
title: Simpler blogging with Working Copy
summary: Combining Workflow and Working Copy makes for powerful, easy blogging from iOS with a GitHub Pages blog
category: General
tags: reference
date: 2017-11-17 12:36:04-0700
---

I have [written]({% post_url 2017-01-06-using-workflow-to-publish-to-github-pages %}) [before]({% post_url 2017-01-12-public-drafts-with-a-github-pages-blog %}) about my attempts to publish to my GitHub Pages blog from iOS. I have recently started using [Working Copy](https://workingcopyapp.com/) to make this even easier. Basically, I am trying to remove all of my excuses in the hopes that I will be more diligent in posting to my blog.

There are three pieces to my new process that I want to explore:

1. [Microblog posts](#microblog-posts)
2. [New drafts](#new-drafts)
3. [Publishing](#publishing)

## Microblog posts
Since September 2016, I have been publishing [microblog](/microblog) posts to my own site in addition to sharing them on [Twitter](https://twitter.com/bsndesign) or [Instagram](https://instagram.com/sketchnotable), and more recently on [Micro.blog](https://micro.blog/bsn). This has come as a direct result of listening to [Manton Reece](http://manton.org) and agreeing with his thoughts on [owning your content](http://www.manton.org/2017/02/owning-your-content-matters-right-now.html). I want to continue the simplicity of being able to post a thought quickly, particularly with an image since I am often sharing my [sketchnotes](/tags/sketchnotes).

Prior to using Working Copy, my process involved [Workflow](https://workflow.is) recipes that made use of the GitHub API to post the content to my site repository. Essentially, I still use the same process in terms of taking the text or images and publishing them to my site. But my [new Workflow recipe](/resources/microblog-post-in-working-copy.wflow) is considerably simpler, and leverages Working Copy and [X-Callback-URLs](http://x-callback-url.com/) to simplify the process.

## New drafts
My favorite writing app, [iA Writer](https://ia.net/writer/), gives me great flexibility in writing my posts. I have gone back and forth on storing my drafts just in iA Writer using iCloud, or having them live in my site repository. Thanks to iA Writer’s feature of opening directly a file from another app, and Working Copy serving as a document provider, I can create a draft in Working Copy and edit it in iA Writer. As of now, my current process is to create a draft in iA Writer using [this Workflow](/resources/new-draft-in-ia-writer.wflow). When I feel like it is ready, I will publish it as a draft to my site using [this Workflow](/resources/publish-draft-in-working-copy.wflow). That gives me the chance to see it in context on my site, together with all images and links and make sure that everything looks good and works properly.

## Publishing
The final step is taking my post from draft status to published. As I mentioned, at this point the post is live on my site in the Drafts section, so I can proofread and check everything. I do my editing either in Working Copy or iA Writer, committing the changes back to GitHub. When I am finally ready to pull the trigger, [this Workflow](/resources/publish-post-in-working-copy.wflow) essentially moves the file from the Drafts folder to the Posts folder, and edits the file name a bit to make it an official post on my blog. The Workflow takes me to my site at the end so I can see the post one last time in all its published glory.

## Summary
Using Working Copy on my iPad / iPhone means that I always have the entire source code of my site with me. It has made life so much easier when I want to edit or tweak the site. Since I prefer to write in [Markdown](https://en.wikipedia.org/wiki/Markdown), and to do everything on an iOS device, this has been the ideal setup for me. Simple integrations with Workflow keep process frictionless. Hopefully this is enough to help ensure that I post more often to my blog.

Just for reference, here are all of the Workflow recipes I am currently using for this process:

- [Microblog post](/resources/microblog-post-in-working-copy.wflow)
- [New draft](/resources/new-draft-in-ia-writer.wflow)
- [Publish draft](/resources/publish-draft-in-working-copy.wflow)
- [Publish post](/resources/publish-post-in-working-copy.wflow)
