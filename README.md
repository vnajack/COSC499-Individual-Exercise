# COSC499 Individual Exercise

## General Information

This individual Git exercise is a small programming assignment to ensure I am familiar with how to use Git by cloning the repository locally, creating and working on branches, and pushing my work appropriately.

A [video](https://1drv.ms/v/s!AlO7D5ntW4NmkcJJWHisKMukBTMiQw?e=alptPq) is included as a short demo to show:
* my Github account with the repository
* the program running
* how to make a simple change locally and push to origin
* how to make an inline comment in my code
* how to commit the change and push to origin
* the results of the successful push
* the README

## Language and Modules

This application was created with the following language and module versions:

- Python 3.10.7

## Features

This application presents itself as a mini simulation where the user starts by becoming the owner of a winery. With a list of 5 wine names and wine scores, the program creates a list of Wine objects (with attributes ID, name, and score). This list can be printed neatly and read easily with the list name on top.

The user is asked how they would like to sort the list: by name (ascending) or by score (descending). Based on the user's response, the program will either sort the list and change the name of the list accordingly, leave the list as is, or ask the user again because it didn't understand the input. After sorting the list, the user is prompted to sort again until the user indicates they do not want to sort the list anymore.