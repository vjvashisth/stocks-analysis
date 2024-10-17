# Multi-Agent Workflow for Stock Analysis

## Overview

This project implements a **Multi-Agent Workflow for Stock Analysis**, designed to automate stock data processing tasks using a modular approach with AWS integration. The workflow fetches and analyzes stock data, utilizing various AWS services and Python-based tools to provide insights on stock performance.

## Objectives

1. **Design and Implementation**
   - Develop a low-level design for the multi-agent workflow.
   - Implement the workflow using a framework that supports parallel and sequential execution of tasks.

2. **Tool Development**
   - Create 3-4 agents (tools) to perform specific tasks that run both sequentially and in parallel.

3. **Stock Data Processing**
   - Automate the search for the top 10 performing stocks using Google Search.
   - Fetch stock data from Yahoo Finance for the identified stocks.
   - Save each stock's data as a CSV file with the correct ticker symbol.
   - Normalize stock prices and identify the best-performing stock over the past 3 months.

4. **AWS Integration**
   - Leverage AWS services like EventBridge, Lambda, S3, DynamoDB, and SQS for automation and data processing.
   - Implement additional features such as Lifecycle Rules in S3, TTL in DynamoDB, and AWS Step Functions for orchestration.

## Solution

<img width="863" alt="image" src="https://github.com/user-attachments/assets/735db2d8-8ebc-4796-a396-39db882d8d35">

