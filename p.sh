# shell script for publishing via phone
set -ue
title=$1
f=_posts/$(date +%Y-%m-%d)-$title.html
cp template.html _posts/$(date +%Y-%m-%d)-$title.html
sed -i s/TITLE/$title/ $f
vim $f
git add $f
git commit -m post

