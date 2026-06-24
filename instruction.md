A web server access log in Apache common/combined format is at /app/access.log. Parse it and write a JSON summary to /app/report.json.

The output must be a single JSON object with exactly these three keys:

- "total_requests" (integer): the number of request lines in the log. Count every non-empty line.
- "unique_ips" (integer): the number of distinct client IP addresses. The client IP is the first whitespace-separated field of each line.
- "top_path" (string): the request path that appears most often. The path is the target of the request line, e.g. "/index.html" from "GET /index.html HTTP/1.1".

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the count of non-empty lines in /app/access.log.
3. "unique_ips" equals the number of distinct client IP addresses in the log.
4. "top_path" equals the most frequently requested path in the log.
