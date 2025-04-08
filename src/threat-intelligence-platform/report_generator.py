from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_cors import CORS
import psycopg2
from fpdf import FPDF
import csv
from datetime import datetime
import os

# Keep all your existing code and add these new functions:

class ThreatReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Threat Intelligence Report", ln=True, align="C")
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")
        
    def add_threat(self, threat, score, vulnerability=None, likelihood=None, impact=None, date=None):
        self.set_font("Arial", "B", 12)
        self.cell(200, 10, f"Threat: {threat}", ln=True)
        self.set_font("Arial", "", 10)
        self.cell(200, 8, f"Risk Score: {score}", ln=True)
        
        if vulnerability:
            self.cell(200, 8, f"Vulnerability: {vulnerability}", ln=True)
        if likelihood:
            self.cell(200, 8, f"Likelihood: {likelihood}", ln=True)
        if impact:
            self.cell(200, 8, f"Impact: {impact}", ln=True)
        if date:
            self.cell(200, 8, f"Date: {date}", ln=True)
        
        self.ln(5)
        
    def add_mitigation(self, threat, strategies):
        self.set_font("Arial", "B", 12)
        self.cell(200, 10, f"Mitigation for: {threat}", ln=True)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, f"Strategy: {strategies}")
        self.ln(5)
        
    def add_section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)
