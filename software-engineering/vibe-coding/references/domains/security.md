# Security

Quick guidance for security-sensitive projects.
Load when: handling user data, auth, payments, sensitive operations.

## Security Mindset

```
Assume:
- All input is malicious
- All users will try to break things
- Secrets will be exposed if in code
- Dependencies have vulnerabilities
- You will be breached (limit blast radius)
```

## Input Validation

```
At EVERY boundary (API, form, file upload):

[ ] Validate type, format, length, range
[ ] Whitelist allowed values when possible
[ ] Reject unknown fields
[ ] Sanitize for output context (HTML, SQL, shell)
[ ] Fail closed (reject if unsure)

Example:
function validateEmail(email) {
  if (!email) throw new ValidationError('Email required');
  if (typeof email !== 'string') throw new ValidationError('Email must be string');
  if (email.length > 254) throw new ValidationError('Email too long');
  if (!EMAIL_REGEX.test(email)) throw new ValidationError('Invalid email format');
  return email.toLowerCase().trim();
}
```

## Common Vulnerabilities

### SQL Injection
```
BAD:
query(`SELECT * FROM users WHERE id = ${id}`)
query("SELECT * FROM users WHERE id = " + id)

GOOD:
query('SELECT * FROM users WHERE id = ?', [id])
query('SELECT * FROM users WHERE id = $1', [id])
```

### XSS (Cross-Site Scripting)
```
BAD:
element.innerHTML = userInput
<div dangerouslySetInnerHTML={{__html: userInput}} />

GOOD:
element.textContent = userInput
<div>{userInput}</div>  // React auto-escapes
// If HTML needed: sanitize with DOMPurify
```

### Path Traversal
```
BAD:
const file = path.join('/uploads', req.params.filename)
// User sends: ../../../etc/passwd

GOOD:
const filename = path.basename(req.params.filename)
const file = path.join('/uploads', filename)
// Verify path is still within uploads dir
```

### Command Injection
```
BAD:
exec(`convert ${filename} output.png`)
// User sends: file.jpg; rm -rf /

GOOD:
execFile('convert', [filename, 'output.png'])
// Or use library that doesn't spawn shell
```

## Authentication

```
Passwords:
[ ] Hash with bcrypt or argon2 (NOT MD5, SHA1)
[ ] Salt is automatic with bcrypt
[ ] Never log passwords
[ ] Never store plaintext

const hash = await bcrypt.hash(password, 12);
const valid = await bcrypt.compare(input, hash);

Sessions/Tokens:
[ ] Short-lived access tokens (15min-1hr)
[ ] Refresh tokens for renewal
[ ] Secure, httpOnly cookies
[ ] Invalidate on password change
[ ] Invalidate on logout (server-side)

Rate limiting:
[ ] Limit login attempts (5/minute)
[ ] Lockout after repeated failures
[ ] CAPTCHA after threshold
[ ] Alert on brute force patterns
```

## Authorization

```
Check on EVERY request:
1. Is user authenticated?
2. Is user authorized for this resource?
3. Is user authorized for this action?

Common mistakes:
- Check once at login, assume forever
- Check action but not resource ownership
- Trust client-side roles

Pattern:
async function getOrder(userId, orderId) {
  const order = await db.orders.findById(orderId);
  if (!order) throw new NotFoundError();
  if (order.userId !== userId) throw new ForbiddenError();
  return order;
}
```

## Secrets Management

```
NEVER:
- Hardcode secrets in code
- Commit secrets to git
- Log secrets
- Include in error messages
- Store in frontend code

DO:
- Use environment variables
- Use secrets manager (AWS Secrets Manager, Vault)
- Rotate regularly
- Different secrets per environment
- Audit access

// Good
const apiKey = process.env.API_KEY;
if (!apiKey) throw new Error('API_KEY not configured');
```

## Data Protection

```
At rest:
[ ] Encrypt sensitive data in database
[ ] Encrypt backups
[ ] Secure key management

In transit:
[ ] HTTPS everywhere (no HTTP)
[ ] TLS 1.2+ only
[ ] Valid certificates

In logs:
[ ] No passwords
[ ] No tokens/API keys
[ ] No PII (or masked)
[ ] No credit card numbers
[ ] No raw request bodies with sensitive data

Masking example:
function maskEmail(email) {
  const [user, domain] = email.split('@');
  return `${user[0]}***@${domain}`;
}
// alice@example.com -> a***@example.com
```

## Security Headers

```
Essential headers:
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000

Cookie flags:
Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Strict
```

## Dependency Security

```
[ ] Audit regularly: npm audit, pip-audit
[ ] Update dependencies (patch and minor)
[ ] Major updates: review changelog
[ ] Use lockfiles (package-lock.json, poetry.lock)
[ ] Monitor for new vulnerabilities
[ ] Remove unused dependencies
```

## Security Checklist

```
Before shipping:
[ ] No hardcoded secrets
[ ] All user input validated
[ ] SQL uses parameterized queries
[ ] HTML output escaped
[ ] Auth on all protected routes
[ ] Authorization checks resource ownership
[ ] Passwords properly hashed
[ ] HTTPS enforced
[ ] Security headers set
[ ] Dependencies audited
[ ] Sensitive data encrypted
[ ] Logs don't contain secrets
[ ] Error messages don't expose internals
[ ] Rate limiting on sensitive endpoints
```

## Incident Response

```
If compromised:
1. Contain: Disable affected systems/accounts
2. Assess: What was accessed?
3. Rotate: All potentially exposed secrets
4. Notify: Users if their data affected
5. Fix: Root cause
6. Learn: Post-mortem, improve defenses
```
