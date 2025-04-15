# Nmap Scan Summary

## Port 5000 – Werkzeug HTTP Server (Python)  
**Risk Level:** Medium

**Overview:**  
Werkzeug is a lightweight server typically bundled with Flask for development use only. It is not designed for scalability or secure web hosting, making it risky to expose on public networks.

**Recommended Mitigation:**
- Avoid using Werkzeug in production environments.
- Switch to a battle-tested WSGI server such as uWSGI or Gunicorn.
- Configure firewalls to restrict external access to development ports.

---

## Port 3000 – Node.js Express Framework (HTTP)  
**Risk Level:** Medium

**Overview:**  
This port is commonly utilized by developers working with Node.js and Express to host local web applications. When such ports are left open to external access, they often expose development settings not intended for production, which may lack essential security features.

**Recommended Mitigation:**
- Ensure the deployment follows production best practices.
- Enable HTTPS to secure data in transit.
- Apply rate-limiting to prevent abuse or brute force attacks.
- Sanitize all incoming data to avoid injection threats.
- Route external traffic through a hardened reverse proxy like Nginx or Apache.

---

# Burp Suite Scan Results

## 1. Reflected Cross-Site Scripting (XSS)  
**Severity:** High

**Description:**  
The application echoes user input from the `q` query parameter directly into the webpage without filtering potentially harmful content.

**Example Request:**  
`GET /search?q=<script>alert(1)</script>`

**Impact:**  
Could allow attackers to execute scripts in a user’s browser, leading to stolen credentials, session hijacking, or redirection to malicious sites.

---

## 2. Directory Listing Enabled  
**Severity:** Medium

**Location:**  
`http://127.0.0.1:3000/static/`

**Impact:**  
The server shows the contents of a folder, which could include configuration files or other sensitive resources meant to stay hidden.

---

## 3. Missing Secure Cookie Attribute  
**Severity:** Medium

**Issue:**  
Cookies issued by the server are missing the `Secure` flag, which ensures they are only sent over encrypted connections.

**Example:**  
`Set-Cookie: sessionid=abc123; HttpOnly`

**Impact:**  
If accessed over HTTP, cookies could be intercepted via man-in-the-middle (MitM) attacks.

---

## 4. Server Version Disclosure  
**Severity:** Low

**Header Info:**  
`Server: Werkzeug/3.1.3 Python/3.13.1`

**Impact:**  
Attackers can use version-specific vulnerabilities when software details are exposed in HTTP response headers.

---

## 5. Missing CSRF Protection  
**Severity:** Medium

**Endpoints Affected:**  
`/login`, `/register`

**Impact:**  
An attacker could forge requests that trick authenticated users into unknowingly performing actions, such as submitting forms without their consent.

---

# OWASP ZAP Scan Results

## High Risk

### 1. Cross-Site Scripting (Reflected)  
**URL:** `http://127.0.0.1:3000/search?q=<script>alert(1)</script>`  
**Description:**  
The server returns user input in the response without escaping HTML, allowing script injection.  
**Solution:** Validate and sanitize all input. Use proper encoding when displaying user-supplied data.

---

## Medium Risk

### 2. Insecure Cookies  
**URL:** `http://127.0.0.1:3000/`  
**Description:**  
Session cookies are transmitted over HTTP, lacking security attributes.  
**Solution:** Add `Secure`, `HttpOnly`, and `SameSite=Strict` attributes to all session cookies.

---

### 3. Missing CSRF Token  
**URL:** `http://127.0.0.1:3000/login`  
**Description:**  
Login forms are missing CSRF tokens, leaving them susceptible to forged form submissions.  
**Solution:** Implement CSRF tokens and validate them for each state-changing request.

---

## Low Risk

### 4. Server Version Disclosure via HTTP Header  
**URL:** `http://127.0.0.1:3000/`  
**Description:**  
Reveals the web server and language version in response headers.  
**Solution:** Mask or remove version details in server responses.

---

### 5. Directory Browsing  
**URL:** `http://127.0.0.1:3000/static/`  
**Description:**  
Lists all files in a directory, potentially exposing sensitive files.  
**Solution:** Turn off directory listing in the server settings or web config.

---

## Informational

### 6. X-Frame-Options Header Not Set  
**Risk:**  
Omission of this header means the site may be loaded in a frame or iframe, which opens the door to clickjacking attacks.  
**Solution:** Set `X-Frame-Options` to `DENY` or `SAMEORIGIN` to control framing behavior.
