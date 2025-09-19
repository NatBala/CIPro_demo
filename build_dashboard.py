import html

import random

import re

from pathlib import Path



HTML = """

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Capital Group | Dashboard</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">

    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&display=swap" rel="stylesheet">

    <style>

        :root {

            --navy-900: #002d62;

            --navy-800: #003973;

            --navy-700: #004b88;

            --navy-600: #0b5ea8;

            --navy-500: #0f6cb8;

            --navy-200: #c8def5;

            --blue-50: #f4f8ff;

            --blue-100: #e9f2ff;

            --neutral-25: #f6f8fb;

            --neutral-50: #f0f3f8;

            --neutral-100: #e3e8f0;

            --neutral-300: #c5cfdd;

            --neutral-500: #7d8899;

            --neutral-700: #4a566a;

            --neutral-900: #1f2a3d;

            --accent-magenta: #b02374;

            --accent-cyan: #86d9d6;

            --white: #ffffff;

            --shadow-panel: 0 24px 54px rgba(9, 38, 74, 0.12);

            --shadow-card: 0 18px 42px rgba(12, 46, 92, 0.14);

            --radius-panel: 22px;

            --radius-card: 18px;

        }



        * {

            box-sizing: border-box;

        }



        body {

            margin: 0;

            font-family: "Source Sans Pro", "Segoe UI", Tahoma, sans-serif;

            color: var(--neutral-900);

            background: var(--neutral-25);

        }



        a {

            color: inherit;

            text-decoration: none;

        }



        button {

            font: inherit;

        }



        svg {

            display: block;

        }



        .hidden {

            display: none !important;

        }



        .auth-wrapper {

            min-height: 100vh;

            background: radial-gradient(circle at top, rgba(13, 102, 176, 0.08), rgba(4, 56, 111, 0.22));

            display: grid;

            place-items: center;

            padding: 48px 16px;

        }



        .login-card {

            width: min(440px, 100%);

            background: var(--white);

            border-radius: 22px;

            box-shadow: 0 32px 60px rgba(9, 38, 74, 0.18);

            padding: 44px 38px;

            display: grid;

            gap: 26px;

        }



        .login-header {

            display: grid;

            gap: 12px;

            text-align: center;

        }



        .login-header svg {

            width: 54px;

            height: 54px;

            margin: 0 auto;

        }



        .login-header h2 {

            margin: 0;

            font-size: 26px;

            color: var(--navy-800);

            font-weight: 700;

        }



        .login-header p {

            margin: 0;

            color: var(--neutral-600);

            font-size: 15px;

        }



        .login-form {

            display: grid;

            gap: 18px;

        }



        .login-label {

            font-size: 13px;

            font-weight: 600;

            letter-spacing: 0.4px;

            text-transform: uppercase;

            color: var(--neutral-600);

        }



        .login-input {

            width: 100%;

            padding: 14px 16px;

            border-radius: 12px;

            border: 1px solid var(--neutral-100);

            font-size: 16px;

            background: var(--neutral-50);

            transition: border 0.2s ease, box-shadow 0.2s ease;

        }



        .login-input:focus {

            outline: none;

            border-color: var(--navy-600);

            box-shadow: 0 0 0 3px rgba(15, 108, 184, 0.12);

        }



        .login-submit {

            margin-top: 6px;

            padding: 14px 18px;

            border-radius: 14px;

            border: none;

            background: var(--navy-600);

            color: var(--white);

            font-weight: 700;

            letter-spacing: 0.5px;

            cursor: pointer;

            box-shadow: inset 0 -2px 0 rgba(255, 255, 255, 0.2);

        }



        .login-submit:hover {

            background: var(--navy-700);

        }



        .login-error {

            min-height: 20px;

            color: #c53b3b;

            font-size: 14px;

            font-weight: 600;

            text-align: center;

        }



        .login-meta {

            font-size: 13px;

            color: var(--neutral-600);

            text-align: center;

        }



        @media (max-width: 540px) {

            .login-card {

                padding: 36px 26px;

            }

        }



        .page {

            min-height: 100vh;

        }



        .topbar {

            position: sticky;

            top: 0;

            z-index: 20;

            background: var(--white);

            border-bottom: 1px solid rgba(9, 46, 92, 0.12);

        }



        .topbar-inner {

            max-width: 1280px;

            margin: 0 auto;

            padding: 18px 36px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 28px;

        }



        .brand {

            display: inline-flex;

            align-items: center;

            gap: 14px;

            min-width: 215px;

        }



        .brand-mark svg {

            width: 46px;

            height: 46px;

        }



        .brand-text {

            display: flex;

            flex-direction: column;

            font-size: 12px;

            letter-spacing: 1.8px;

            font-weight: 700;

            color: var(--navy-900);

            text-transform: uppercase;

            line-height: 1.15;

        }



        .primary-nav {

            display: flex;

            align-items: center;

            gap: 30px;

            flex: 1;

        }



        .nav-link {

            display: inline-flex;

            align-items: center;

            gap: 6px;

            font-weight: 600;

            font-size: 16px;

            color: var(--neutral-700);

            padding: 6px 0;

        }



        .nav-link svg {

            width: 11px;

            height: 11px;

        }



        .topbar-actions {

            display: inline-flex;

            align-items: center;

            gap: 20px;

        }



        .region-pill {

            display: inline-flex;

            align-items: center;

            gap: 8px;

            font-size: 14px;

            color: var(--neutral-600);

            white-space: nowrap;

        }



        .region-pill svg {

            width: 20px;

            height: 20px;

        }



        .link-chevron {

            display: inline-flex;

            align-items: center;

            gap: 6px;

            font-weight: 600;

            color: var(--navy-600);

        }



        .logout-btn {

            display: inline-flex;

            align-items: center;

            justify-content: center;

            padding: 10px 26px;

            border-radius: 999px;

            border: none;

            font-weight: 600;

            color: var(--white);

            background: var(--navy-900);

            box-shadow: inset 0 -2px 0 rgba(255, 255, 255, 0.18);

            cursor: pointer;

        }



        .user-chip {

            font-weight: 600;

            color: var(--neutral-700);

        }



        .cart-btn {

            display: inline-flex;

            align-items: center;

            gap: 8px;

            padding: 7px 18px;

            border-radius: 999px;

            border: 1px solid rgba(9, 46, 92, 0.25);

            font-weight: 600;

            color: var(--navy-700);

            background: var(--white);

        }



        .cart-btn svg {

            width: 22px;

            height: 22px;

        }



        .icon-btn {

            border: none;

            background: none;

            padding: 0;

            color: var(--navy-700);

            display: inline-flex;

            cursor: pointer;

        }



        .icon-btn svg {

            width: 24px;

            height: 24px;

        }



        .layout {

            max-width: 1280px;

            margin: 0 auto;

            display: grid;

            grid-template-columns: 232px 1fr;

            gap: 32px;

            padding: 36px 36px 80px;

        }



        .sidebar {

            background: linear-gradient(180deg, #022d5d 0%, #04386f 100%);

            border-radius: 0 22px 22px 0;

            padding: 38px 26px;

            color: rgba(255, 255, 255, 0.88);

            display: flex;

            flex-direction: column;

            gap: 30px;

            box-shadow: 0 24px 40px rgba(4, 28, 58, 0.28);

        }



        .sidebar-group {

            display: grid;

            gap: 8px;

        }



        .sidebar-link {

            display: inline-flex;

            align-items: center;

            gap: 14px;

            padding: 12px 16px;

            border-radius: 14px;

            color: inherit;

            font-weight: 600;

            transition: background 0.2s ease, color 0.2s ease;

        }



        .sidebar-link svg {

            width: 20px;

            height: 20px;

            opacity: 0.85;

        }



        .sidebar-link.active,

        .sidebar-link:hover {

            background: rgba(255, 255, 255, 0.18);

            color: var(--white);

        }



        .sidebar-divider {

            height: 1px;

            background: rgba(255, 255, 255, 0.26);

            margin: 18px 0 10px;

        }



        .content {

            display: grid;

            gap: 28px;

        }



        .surface {

            background: var(--white);

            border-radius: var(--radius-panel);

            padding: 32px;

            box-shadow: var(--shadow-panel);

        }



        .welcome-row {

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 24px;

        }



        .welcome-row h1 {

            margin: 0;

            font-size: 34px;

            font-weight: 700;

            color: var(--navy-800);

        }



        .alert-link {

            display: inline-flex;

            align-items: center;

            gap: 10px;

            font-weight: 600;

            color: var(--navy-600);

            white-space: nowrap;

        }



        .alert-link svg {

            width: 20px;

            height: 20px;

        }



        .section-header {

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 16px;

            margin-bottom: 24px;

        }



        .section-header h2 {

            margin: 0;

            font-size: 26px;

            font-weight: 700;

            color: var(--navy-800);

        }



        .section-header .link-chevron svg {

            width: 16px;

            height: 16px;

        }



        .feed-grid {\n            position: relative;\n        }\n\n        .feed-loading, .feed-error {\n            grid-column: 1 / -1;\n            background: var(--white);\n            border-radius: var(--radius-card);\n            box-shadow: var(--shadow-card);\n            padding: 32px;\n            font-weight: 600;\n            color: var(--neutral-700);\n        }\n\n        .feed-loading::before {\n            content: 'Loading recommendations...';\n        }\n\n        .feed-error {\n            color: #c23f3f;\n        }\n\n        .feed-grid {

            display: grid;

            grid-template-columns: repeat(4, minmax(0, 1fr));

            gap: 24px;

        }



        .feed-card {

            background: var(--white);

            border-radius: var(--radius-card);

            box-shadow: var(--shadow-card);

            overflow: hidden;

            display: block;

        }





        .feed-card-link {

            display: grid;

            height: 100%;

            color: inherit;

            text-decoration: none;

        }



        .feed-card-link:hover .feed-card-title {

            color: var(--navy-600);

        }



        .feed-card-link:focus-visible {

            outline: 3px solid rgba(15, 108, 184, 0.3);

            outline-offset: 4px;

        }



        .feed-card img {

            width: 100%;

            height: 100%;

            object-fit: cover;

        }



        .feed-card-body {

            padding: 24px;

            display: grid;

            gap: 12px;

        }



        .feed-card-eyebrow {

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 0.6px;

            color: var(--neutral-500);

            text-transform: uppercase;

        }



        .feed-card-title {

            margin: 0;

            font-size: 20px;

            font-weight: 600;

            color: var(--neutral-900);

            line-height: 1.35;

        }



        .text-link {

            display: inline-flex;

            align-items: center;

            gap: 8px;

            font-weight: 600;

            color: var(--navy-600);

        }



        .text-link svg {

            width: 16px;

            height: 16px;

        }



        .course-grid {

            display: grid;

            grid-template-columns: repeat(2, minmax(0, 1fr));

            gap: 22px;

        }



        .course-card {

            position: relative;

            border-radius: var(--radius-card);

            padding: 30px;

            background: linear-gradient(160deg, var(--blue-100) 0%, var(--blue-50) 100%);

            box-shadow: 0 20px 44px rgba(10, 43, 84, 0.16);

            display: grid;

            gap: 18px;

        }



        .course-badge {

            position: absolute;

            top: 22px;

            right: 26px;

            background: var(--accent-magenta);

            color: var(--white);

            padding: 6px 14px;

            border-radius: 999px;

            font-size: 11px;

            letter-spacing: 1.3px;

            font-weight: 700;

        }



        .course-card h3 {

            margin: 0;

            font-size: 22px;

            font-weight: 700;

            color: var(--navy-900);

            line-height: 1.35;

        }



        .course-card p {

            margin: 0;

            font-size: 16px;

            color: var(--neutral-600);

            line-height: 1.55;

        }



        .primary-btn {

            display: inline-flex;

            align-items: center;

            justify-content: center;

            padding: 12px 28px;

            border-radius: 12px;

            background: var(--navy-800);

            color: var(--white);

            font-weight: 700;

            letter-spacing: 0.5px;

            text-transform: uppercase;

            font-size: 13px;

            box-shadow: inset 0 -2px 0 rgba(255, 255, 255, 0.22);

        }



        .split-grid {

            display: grid;

            grid-template-columns: 2fr 1fr;

            gap: 24px;

        }



        .hero-card {

            position: relative;

            border-radius: var(--radius-panel);

        padding: 42px 38px;

            color: var(--white);

            background: radial-gradient(circle at 20% 25%, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0) 50%),

                linear-gradient(145deg, #04366c, #0a5aa8 70%, #1176c6 100%);

            overflow: hidden;

            box-shadow: var(--shadow-card);

        }



        .hero-card::after {

            content: "";

            position: absolute;

            width: 340px;

            height: 340px;

            border-radius: 50%;

            background: rgba(255, 255, 255, 0.12);

            top: -140px;

            right: -110px;

        }



        .hero-card span {

            font-size: 12px;

            letter-spacing: 0.7px;

            text-transform: uppercase;

            font-weight: 700;

            opacity: 0.85;

        }



        .hero-card h3 {

            margin: 14px 0 18px;

            font-size: 28px;

            font-weight: 700;

        }



        .hero-card p {

            margin: 0 0 26px;

            max-width: 540px;

            font-size: 16px;

            line-height: 1.6;

        }



        .hero-actions {

            display: inline-flex;

            gap: 14px;

            flex-wrap: wrap;

            position: relative;

            z-index: 1;

        }



        .outline-btn {

            display: inline-flex;

            align-items: center;

            justify-content: center;

            padding: 12px 26px;

            border-radius: 12px;

            border: 2px solid rgba(255, 255, 255, 0.92);

            color: var(--white);

            font-weight: 700;

            text-transform: uppercase;

            letter-spacing: 0.5px;

            font-size: 13px;

        }



        .side-stack {

            display: grid;

            gap: 20px;

        }



        .info-card {

            background: var(--white);

            border-radius: var(--radius-panel);

            padding: 28px;

            box-shadow: var(--shadow-panel);

            display: grid;

            gap: 18px;

        }



        .info-card h4 {

            margin: 0;

            font-size: 22px;

            font-weight: 700;

            color: var(--navy-900);

        }



        .info-card .label {

            font-size: 12px;

            letter-spacing: 0.6px;

            text-transform: uppercase;

            font-weight: 700;

            color: var(--neutral-500);

        }



        .info-divider {

            height: 1px;

            background: var(--neutral-100);

            margin: 4px 0;

        }



        .info-card a {

            font-weight: 600;

            color: var(--navy-600);

            display: inline-flex;

            align-items: center;

            gap: 8px;

        }



        .info-card a svg {

            width: 14px;

            height: 14px;

        }



        @media (max-width: 1180px) {

            .layout {

                grid-template-columns: 210px 1fr;

            }



            .feed-grid {\n            position: relative;\n        }\n\n        .feed-loading, .feed-error {\n            grid-column: 1 / -1;\n            background: var(--white);\n            border-radius: var(--radius-card);\n            box-shadow: var(--shadow-card);\n            padding: 32px;\n            font-weight: 600;\n            color: var(--neutral-700);\n        }\n\n        .feed-loading::before {\n            content: 'Loading recommendations...';\n        }\n\n        .feed-error {\n            color: #c23f3f;\n        }\n\n        .feed-grid {

                grid-template-columns: repeat(2, minmax(0, 1fr));

            }



            .split-grid {

                grid-template-columns: 1fr;

            }

        }



        @media (max-width: 960px) {

            .topbar-inner {

                flex-wrap: wrap;

                gap: 18px;

            }



            .primary-nav {

                order: 3;

                width: 100%;

                flex-wrap: wrap;

            }



            .topbar-actions {

                order: 2;

                flex-wrap: wrap;

            }



            .layout {

                grid-template-columns: 1fr;

                padding: 28px;

            }



            .sidebar {

                flex-direction: row;

                border-radius: 22px;

                overflow-x: auto;

            }

        }



        @media (max-width: 720px) {

            .feed-grid,

            .course-grid {

                grid-template-columns: 1fr;

            }



            .welcome-row {

                flex-direction: column;

                align-items: flex-start;

            }

        }

    </style>

</head>

<body>

    <div class="auth-wrapper" id="auth-wrapper">

        <div class="login-card">

            <div class="login-header">

                <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                    <rect x="4" y="4" width="28" height="28" rx="4" fill="#0d66b0"></rect>

                    <rect x="20" y="20" width="28" height="28" rx="4" fill="#0691d2"></rect>

                    <rect x="36" y="36" width="24" height="24" rx="4" fill="#52c0f0"></rect>

                </svg>

                <h2>Capital Group Advisor Access</h2>

                <p>Sign in as Nat or K to view your personalized experience.</p>

            </div>

            <form class="login-form" id="login-form">

                <div>

                    <label class="login-label" for="username">Username</label>

                    <input class="login-input" type="text" id="username" name="username" autocomplete="username" placeholder="Enter nat or k" required>

                </div>

                <div>

                    <label class="login-label" for="password">Password</label>

                    <input class="login-input" type="password" id="password" name="password" autocomplete="current-password" placeholder="Password" required>

                </div>

                <button class="login-submit" type="submit">Log In</button>

                <div class="login-error" id="login-error"></div>

            </form>

            <div class="login-meta">

                Use <strong>nat / capital123</strong> or <strong>k / advisor456</strong> to continue.

            </div>

        </div>

    </div>

    <div class="page hidden" id="dashboard">

        <header class="topbar">

            <div class="topbar-inner">

                <a class="brand" href="#">

                    <span class="brand-mark">

                        <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                            <rect x="4" y="4" width="28" height="28" rx="4" fill="#0d66b0"></rect>

                            <rect x="20" y="20" width="28" height="28" rx="4" fill="#0691d2"></rect>

                            <rect x="36" y="36" width="24" height="24" rx="4" fill="#52c0f0"></rect>

                        </svg>

                    </span>

                    <span class="brand-text">

                        <span>CAPITAL GROUP</span>

                        <span>AMERICAN FUNDS</span>

                    </span>

                </a>

                <nav class="primary-nav">

                    <a class="nav-link" href="#">

                        <span>For You</span>

                        <svg viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                    <a class="nav-link" href="#">

                        <span>Investments</span>

                        <svg viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                    <a class="nav-link" href="#">

                        <span>Insights</span>

                        <svg viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                    <a class="nav-link" href="#">

                        <span>Tools &amp; Resources</span>

                        <svg viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                    <a class="nav-link" href="#">

                        <span>About Us</span>

                        <svg viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                </nav>

                <div class="topbar-actions">

                    <span class="region-pill">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                            <circle cx="12" cy="12" r="10" stroke="#0f6cb8" stroke-width="1.4" fill="none"></circle>

                            <path d="M4 9.5h16M4 14.5h16" stroke="#0f6cb8" stroke-width="1.1" stroke-linecap="round"></path>

                            <path d="M12 2c2.8 3 3.8 7.4 0 20" stroke="#0f6cb8" stroke-width="1.1" stroke-linecap="round"></path>

                        </svg>

                        <span>US</span>

                        <span>&bull;</span>

                        <span>Financial Professional</span>

                    </span>

                    <a class="link-chevron" href="#">

                        Client Accounts

                        <svg viewBox="0 0 10 6" xmlns="http://www.w3.org/2000/svg"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                    </a>

                    <button class="logout-btn" type="button">Log Out</button>

                    <span class="user-chip" id="user-chip">Nat Bala</span>

                    <span class="cart-btn">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                            <path d="M6 6h15l-2.1 8.5a2 2 0 01-1.94 1.6H9.4a2 2 0 01-1.96-1.64L5.2 3.5H2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>

                            <circle cx="10" cy="20" r="1.6" fill="currentColor"></circle>

                            <circle cx="18" cy="20" r="1.6" fill="currentColor"></circle>

                        </svg>

                        <span>(0)</span>

                    </span>

                    <button class="icon-btn" type="button" aria-label="Search">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                            <circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.8" fill="none"></circle>

                            <path d="M16.5 16.5L21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>

                        </svg>

                    </button>

                </div>

            </div>

        </header>



        <main class="layout">

            <aside class="sidebar">

                <div class="sidebar-group">

                    <a class="sidebar-link active" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 11l8-6 8 6v9H4z" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linejoin="round"></path><path d="M10 20v-6h4v6" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path></svg>

                        <span>For You</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 3l2.4 7H21l-5.4 4 2.2 7L12 18l-5.6 3 2.2-7L3 10h6.6z" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linejoin="round"></path></svg>

                        <span>Insights</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a6 6 0 016 6c0 2.6-1.8 4.8-4.3 5.7L13 20H7l1.3-4.3C5.8 14.8 4 12.6 4 10a6 6 0 016-6z" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                        <span>My Growth Areas</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="4" y="3" width="16" height="12" rx="2" fill="none" stroke="#ffffff" stroke-width="1.6"></rect><path d="M8 21l4-3 4 3" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                        <span>Courses</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M6 9h12M6 15h12" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path><circle cx="6" cy="9" r="1.6" fill="#ffffff"></circle><circle cx="6" cy="15" r="1.6" fill="#ffffff"></circle></svg>

                        <span>Webinars &amp; Events</span>

                    </a>

                </div>

                <div class="sidebar-divider"></div>

                <div class="sidebar-group">

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="#ffffff" stroke-width="1.6"></rect><path d="M7 3v4M17 3v4" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path></svg>

                        <span>Client Accounts</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 6h16v12H4z" fill="none" stroke="#ffffff" stroke-width="1.6"></path><path d="M9 6v12" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path><path d="M4 11h16" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path></svg>

                        <span>Account Resource Center</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 4h14l-2 12H7z" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linejoin="round"></path><path d="M9 20h6" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path></svg>

                        <span>Forms &amp; Literature</span>

                    </a>

                    <a class="sidebar-link" href="#">

                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" fill="none" stroke="#ffffff" stroke-width="1.6"></circle><path d="M12 6v12" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path><path d="M6 12h12" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"></path></svg>

                        <span>Announcements</span>

                    </a>

                </div>

            </aside>



            <div class="content">

                <section class="surface">

                    <div class="welcome-row">

                        <h1 id="welcome-heading">Welcome Nat!</h1>

                        <a class="alert-link" href="#">

                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

                                <path d="M12 4a6 6 0 00-6 6v3.6l-.8 1.6a1 1 0 00.9 1.4h11.8a1 1 0 00.9-1.4l-.8-1.6V10a6 6 0 00-6-6z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>

                                <path d="M10.5 19h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>

                            </svg>

                            <span>2025 proxy vote details</span>

                        </a>

                    </div>

                </section>



                <section class="surface">

                    <div class="section-header">

                        <h2>Your Feed</h2>

                    </div>

                    <div class="feed-grid" id="feed-grid">

                        <!-- FEED_CARDS -->

                    </div>

                </section>



                <section class="surface">

                    <div class="section-header">

                        <h2>Courses</h2>

                        <a class="link-chevron" href="#">

                            View All

                            <svg viewBox="0 0 16 10" xmlns="http://www.w3.org/2000/svg"><path d="M1 5h12m0 0l-3-3m3 3l-3 3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                        </a>

                    </div>

                    <div class="course-grid">

                        <article class="course-card">

                            <span class="course-badge">NEW</span>

                            <h3>Build and lead a high-performing advisory practice</h3>

                            <p>Gain the knowledge and strategies you need to help grow, scale and create lasting value in your business.</p>

                            <a class="primary-btn" href="#">Start Course</a>

                        </article>

                        <article class="course-card">

                            <span class="course-badge">NEW</span>

                            <h3>Introduction to private credit and public-private solutions</h3>

                            <p>Explore the opportunities and challenges of private credit investments and how Public-Private+ Solutions can open the door to new markets for your investors.</p>

                            <a class="primary-btn" href="#">Start Course</a>

                        </article>

                    </div>

                </section>



                <section class="surface">

                    <div class="split-grid">

                        <div class="hero-card">

                            <span>Practice Growth</span>

                            <h3>Assess your skills to grow your business</h3>

                            <p>Identify the skills needed to drive growth in your practice based on our benchmark survey of more than 3,740 advisors and access resources to help you take action.</p>

                            <div class="hero-actions">

                                <a class="primary-btn" href="#">Start Here</a>

                                <a class="outline-btn" href="#">Learn More</a>

                            </div>

                        </div>

                        <div class="side-stack">

                            <section class="info-card">

                                <h4>Your Capital Team</h4>

                                <div>

                                    <span class="label">Advisor Marketing</span><br>

                                    <a href="tel:8004219900">(800) 421-9900</a>

                                </div>

                                <div class="info-divider"></div>

                                <a href="#">

                                    <span>More contacts</span>

                                    <svg viewBox="0 0 16 10" xmlns="http://www.w3.org/2000/svg"><path d="M1 5h12m0 0l-3-3m3 3l-3 3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                                </a>

                            </section>

                            <section class="info-card">

                                <h4>Find opportunities</h4>

                                <p>Plan client conversations around market-moving topics with ready-to-go resources.</p>

                                <a href="#">

                                    <span>Explore now</span>

                                    <svg viewBox="0 0 16 10" xmlns="http://www.w3.org/2000/svg"><path d="M1 5h12m0 0l-3-3m3 3l-3 3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>

                                </a>

                            </section>

                        </div>

                    </div>

                </section>

            </div>

        </main>

    </div>

    <script>

        (function() {

            const credentials = {

                nat: { password: "capital123", displayName: "Nat", chip: "Nat Bala" },

                k: { password: "advisor456", displayName: "K", chip: "K Taylor" }

            };

            const loginForm = document.getElementById("login-form");

            const usernameInput = document.getElementById("username");

            const passwordInput = document.getElementById("password");

            const errorBox = document.getElementById("login-error");

            const authWrapper = document.getElementById("auth-wrapper");

            const dashboard = document.getElementById("dashboard");

            const welcomeHeading = document.getElementById("welcome-heading");

            const userChip = document.getElementById("user-chip");



            if (!loginForm) {

                return;

            }



            loginForm.addEventListener("submit", function(event) {

                event.preventDefault();

                const username = usernameInput.value.trim().toLowerCase();

                const password = passwordInput.value;

                const record = credentials[username];



                if (record && record.password === password) {

                    welcomeHeading.textContent = `Welcome ${record.displayName}!`;

                    userChip.textContent = record.chip;

                    authWrapper.classList.add("hidden");

                    dashboard.classList.remove("hidden");

                    errorBox.textContent = "";

                    loginForm.reset();

                } else {

                    errorBox.textContent = "Invalid username or password.";

                }

            });

        })();

    </script>

</body>

</html>

"""







CORPUS_PATH = Path(__file__).with_name('corpus.txt')



FEED_IMAGES = [

    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1496567641772-04b3caf479c0?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1529429617124-aee0a91b1b43?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1525182008055-f88b95ff7980?auto=format&fit=crop&w=1100&q=80',

    'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1100&q=80',

]



ARROW_ICON = (

    '<svg viewBox="0 0 16 10" xmlns="http://www.w3.org/2000/svg">'

    '<path d="M1 5h12m0 0l-3-3m3 3l-3 3" fill="none" stroke="currentColor" '

    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>'

    '</svg>'

)



FEED_CARD_TEMPLATE = '''                        <article class="feed-card">

                            <a class="feed-card-link" href="{link}"{target}>

                                <img src="{image}" alt="{title}">

                                <div class="feed-card-body">

                                    <span class="feed-card-eyebrow">{category}</span>

                                    <h3 class="feed-card-title">{title}</h3>

                                    <span class="text-link">

                                        <span>Read now</span>

                                        {arrow}

                                    </span>

                                </div>

                            </a>

                        </article>'''



ARTICLE_PATTERN = re.compile(

    r"Title:\s*(.+?)\r?\nPublished Date:\s*(.+?)\r?\n(?:Key URL|Link):\s*(.+?)\r?\nContent:\r?\n(.+?)(?=\r?\n\\?=+|$)",

    re.DOTALL,

)



URL_PATTERN = re.compile(r'https?://[^\s<>"\)]+', re.IGNORECASE)




def load_articles(path: Path):

    if not path.exists():

        return []

    text = path.read_text(encoding='utf-8')

    articles = []

    for title, published, link, content in ARTICLE_PATTERN.findall(text):

        body = content.strip()

        snippet = body.splitlines()[0].strip() if body else ''

        link_value = (link or '').strip()

        if link_value:

            md_match = re.search(r'\((https?://[^)]+)\)', link_value)

            bracket_match = re.search(r'<(https?://[^>]+)>', link_value)

            if md_match:

                link_value = md_match.group(1)

            elif bracket_match:

                link_value = bracket_match.group(1)

        else:

            url_match = URL_PATTERN.search(body)

            link_value = url_match.group(0) if url_match else ''

        articles.append(

            {

                'title': ' '.join(title.split()),

                'published': published.strip(),

                'snippet': snippet,

                'link': link_value,

            }

        )

    return articles




def derive_category(title: str) -> str:

    base = title.split(':', 1)[0].strip() if ':' in title else ' '.join(title.split()[:3]).strip()

    if not base:

        base = 'Insights'

    base = base.upper()

    if len(base) > 40:

        base = base[:37].rstrip() + '...'

    return base



def render_feed_cards(articles) -> str:

    if not articles:

        return ''

    sample_size = min(8, len(articles))

    selected = articles[:sample_size]

    images = FEED_IMAGES.copy()

    random.shuffle(images)

    cards = []

    for index, article in enumerate(selected):

        image_url = images[index % len(images)]

        title_text = html.escape(article['title'])

        category_text = html.escape(derive_category(article['title']))

        raw_link = (article.get('link') or '').strip()

        has_link = bool(raw_link)

        link_href = html.escape(raw_link or '#', quote=True)

        target_attr = ' target="_blank" rel="noopener noreferrer"' if has_link else ''

        card_html = FEED_CARD_TEMPLATE.format(

            image=image_url,

            title=title_text,

            category=category_text,

            arrow=ARROW_ICON,

            link=link_href,

            target=target_attr,

        )

        cards.append(card_html)

    return '\n'.join(cards)



def render_html() -> str:

    articles = load_articles(CORPUS_PATH)

    cards_html = render_feed_cards(articles)

    return HTML.replace('<!-- FEED_CARDS -->', cards_html)





def build(output: Path) -> None:

    output.parent.mkdir(parents=True, exist_ok=True)

    html_output = render_html()

    output.write_text(html_output, encoding="utf-8")

    root_out = Path(__file__).with_name('index.html')

    root_out.write_text(html_output, encoding="utf-8")

    print(f"Created {output}")





if __name__ == "__main__":

    build(Path("dist/index.html"))

