#!/bin/bash
rm -rf report

mkdir -p report

rm -rf allure-report

pytest tests

allure_gen/allure-2.7.0/bin/allure generate report