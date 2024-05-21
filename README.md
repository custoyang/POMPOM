# POMPOM (Engineering Project) - Pill Organizing Machine

<img src="https://media.discordapp.net/attachments/1239019889541513317/1239020375002841170/pomlogo.png?ex=66440a25&is=6642b8a5&hm=6f636111d8000eb7a3b6384e0767db898d9a727fe844b5e8a83bad3df5b33f43&=&format=webp&quality=lossless&width=263&height=196" />


## 🚩 Table of Contents

- [Introduction](#-introduction)
- [Module Installation](#-module-installation)
- [Guidelines](#-guidelines)
- [Features](#-features)
- [Usage](#-usage)
- [Authors](#-authors)

## 🤖 Introduction
POMPOM is a pill-organizing machine controlled by a web application, where users can view pill information on an LCD screen. Users should be able to control the time of pill dispensing and amount of pills dispensed with the web application as the administrator mode. When a pill is dispensed, the number of pills remaining in each compartment should be updated accordingly.

## 📦 Module Installation
pip install flask
pip install flask-sqlalchemy
pip install flask-login
pip install gpiozero

## 🔧 Guidelines
| Language   | Guideline | Tools |
|------------|-----------|-------|
| Python     |[Python Guideline](https://peps.python.org/pep-0008/)           | [Flask](https://flask.palletsprojects.com/en/2.1.x/ )     |
| JavaScript |[JavaScript Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/JavaScript#general_javascript_guidelines)|       |
| CSS        |[CSS Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/CSS)      |       |
| HTML       |[HTML Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/HTML)      |       |

## 🎨 Features
A strong feature in this web application is the ability to edit pill information, such as the specific compartment number, size, name, and time you would like the pills to be automatically dispensed. When the time comes, the motor will spin for that compartment, dropping the proper amount of pills needed.

## 🐾 Usage
In order to run the web app via Flask, you must open ```flask_server/app.py```, running the web app on a local host port.

## 🌏 Authors
Custo Yang
Lance Vu
Maggie Zhang
