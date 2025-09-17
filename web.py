from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP vs IP Protocols</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #283e51, #485563);
            color: white;
            text-align: center;
            padding: 40px;
        }
        h1 { margin-bottom: 25px; }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 90%;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            border-radius: 10px;
            overflow: hidden;
        }
        th, td {
            padding: 14px;
            border: 1px solid rgba(255,255,255,0.3);
            text-align: left;
        }
        th {
            background-color: rgba(0,0,0,0.6);
            color: #ffcc70;
        }
        tr:nth-child(even) {
            background-color: rgba(255,255,255,0.05);
        }
        td:first-child {
            font-weight: bold;
            background-color: rgba(0,0,0,0.3);
            color: #ffcc70;
            width: 25%;
        }
    </style>
</head>
<body>
    <h1>Detailed Comparison: TCP vs IP</h1>
    <table>
        <tr>
            <th>Feature</th>
            <th>TCP</th>
            <th>IP</th>
        </tr>
        <tr>
            <td>Full Form</td>
            <td>Transmission Control Protocol</td>
            <td>Internet Protocol</td>
        </tr>
        <tr>
            <td>Layer</td>
            <td>Transport Layer (Layer 4)</td>
            <td>Network Layer (Layer 3)</td>
        </tr>
        <tr>
            <td>Purpose</td>
            <td>Provides reliable, error-checked, end-to-end communication</td>
            <td>Handles addressing, routing, and delivery of packets</td>
        </tr>
        <tr>
            <td>Connection Type</td>
            <td>Connection-oriented (3-way handshake)</td>
            <td>Connectionless (independent packets)</td>
        </tr>
        <tr>
            <td>Reliability</td>
            <td>Ensures delivery with acknowledgements, retransmission, sequencing</td>
            <td>No guarantee of delivery, may drop or reorder packets</td>
        </tr>
        <tr>
            <td>Error Checking</td>
            <td>Checks both header & data</td>
            <td>IPv4 checks only header, IPv6 no checksum</td>
        </tr>
        <tr>
            <td>Flow & Congestion Control</td>
            <td>Yes, built-in (windowing, congestion control)</td>
            <td>No</td>
        </tr>
        <tr>
            <td>Data Unit</td>
            <td>Segments</td>
            <td>Packets / Datagrams</td>
        </tr>
        <tr>
            <td>Header Size</td>
            <td>20 bytes (minimum)</td>
            <td>IPv4: 20 bytes, IPv6: 40 bytes</td>
        </tr>
        <tr>
            <td>Addressing</td>
            <td>Uses port numbers to identify applications</td>
            <td>Uses IP addresses to identify hosts</td>
        </tr>
        <tr>
            <td>Examples of Use</td>
            <td>HTTP, HTTPS, FTP, SMTP, SSH</td>
            <td>Underlying delivery for all internet communication</td>
        </tr>
    </table>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8080)  # safer to use port 8080
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running at http://localhost:8080 ...")
httpd.serve_forever()
