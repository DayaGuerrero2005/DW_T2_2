@echo off
git init
git branch -M main
git add .
git commit -m "feat(spl): implementar linea de productos Django MediSPL-UNEMI (Practica 4 UNEMI)"
git remote add origin https://github.com/DayaGuerrero2005/GCS_TPE4.git
git push -u origin main
