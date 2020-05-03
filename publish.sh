#!/bin/sh -e

pip install --upgrade twine

twine check dist/*

twine upload dist/*
