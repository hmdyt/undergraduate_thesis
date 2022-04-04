# undergraduate_thesis
- [docker image](https://blog.akashisn.info/entry/2021/12/18/201144)
- [Latex Template](https://github.com/mzks/TexTempJa)
  - uplatex

## build
```bash
latexmk -pdfdvi -outdir=out
```

## GitHub Actionsによるpdf生成
- tagをつけてpushしたら自動的にコンパイル,pdfがreleaseされる
- actionsは[こちら](https://zenn.dev/ganariya/articles/platex-github-action)から拝借して少し変更を加えた
```bash
git tag -a vX.X.X -m "commit comment"
git push origin vX.X.X
```

## script
- 以下のコマンドで ./tex 以下のファイルの句読点を置換する
  - 、。-> ,.
```bash
python3 script/replacer.py --all
```