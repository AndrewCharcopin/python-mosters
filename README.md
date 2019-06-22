# python-mosters
Flowchart: https://drive.google.com/file/d/14nVAomSFOjzgUCL2G29L3WTkesIlg6ew/view?usp=sharing



# ル-ル 
- まず、 git checkout -b <ブランチ名> でブランチを作る。
- git add <file名>
- git commit -m "メッセージ"
- git push origin <ブランチ名>

#python-env
- python 3.7.3
- anaconda3-2019.03
- pygame 1.9.6

#pygame-setup
- cd python-monsters
- brew update && brew upgrade pyenv
- pyenv install 3.7.3
- pyenv local 3.7.3
- pyenv install anaconda3-2019.03
- pyenv local anaconda3-2019.03
- python3 -m pip install -U pygame --user
- python -m pygame.examples.aliens(動作確認)
