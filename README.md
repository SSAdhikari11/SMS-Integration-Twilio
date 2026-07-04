<h1 align="center">SMS Integration for Frappe ERPNext</h1>

<p align="center">
  A custom Frappe application that integrates Twilio SMS APIs with ERPNext. 
</p> 

<hr> 

<h2>🚀 Features</h2> 

<ul>
  <li>Twilio SMS Integration</li>
  <li>Custom Twilio Settings DocType</li>
  <li>Send SMS from Customer Form</li>
  <li>Automatic Contact Number Retrieval</li>
  <li>Secure Credential Storage</li>
  <li>Server-side SMS Processing</li>
</ul>

<h2>🛠 Tech Stack</h2>

<ul>
  <li>Frappe Framework v15</li>
  <li>ERPNext v15</li>
  <li>Python</li>
  <li>Twilio API</li>
</ul>

<h2>📂 Installation</h2>

<pre>
bench get-app https://github.com/SSAdhikari11/Frappe-Twilio-Integration.git

bench --site your-site install-app sms_integration
</pre>

<h2>📦 Install Twilio SDK</h2>

<pre>
bench pip install twilio
</pre>

<h2>⚙️ Configuration</h2>

<p>
Navigate to <strong>Twilio Settings</strong> and configure:
</p>

<table>
  <tr>
    <th>Field</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Account SID</td>
    <td>Twilio Account SID</td>
  </tr>
  <tr>
    <td>Auth Token</td>
    <td>Twilio Authentication Token</td>
  </tr>
  <tr>
    <td>Twilio Number</td>
    <td>SMS-enabled Twilio Number</td>
  </tr>
</table>

<h2>📱 Usage</h2>

<ol>
  <li>Open a Customer record.</li>
  <li>Ensure the linked Contact has a phone number.</li>
  <li>Click <strong>Send SMS</strong>.</li>
  <li>The application sends an SMS using Twilio.</li>
</ol>

<h2>🔄 Workflow</h2>

<pre>
Customer
   ↓
Linked Contact
   ↓
Phone Number
   ↓
Twilio API
   ↓
SMS Delivered
</pre>

<h2>📸 Screenshots</h2>

<p>Add screenshots here:</p>

<ul>
  <li>Twilio Settings</li>
  <img width="1365" height="800" alt="Screenshot 2026-06-03 183726" src="https://github.com/user-attachments/assets/407b57a9-6660-45cb-bb13-cda1442b712f" />

  <li>Customer Form</li>
  <img width="1379" height="900" alt="Screenshot 2026-06-03 183617" src="https://github.com/user-attachments/assets/ae312249-d86f-44aa-a182-ea6daf694656" />

  <li>SMS Delivery Message</li>
  <img width="720" height="1560" alt="WhatsApp Image 2026-06-03 at 18 42 26" src="https://github.com/user-attachments/assets/781a9faa-ee35-43a3-ad3a-66cf7f4d94f2" />

</ul>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>SMS Templates</li>
  <li>Bulk SMS Sending</li>
  <li>SMS Logs</li>
  <li>Delivery Tracking</li>
  <li>Scheduled Notifications</li>
</ul>

<h2>👨‍💻 Author</h2>

<p>
Suraj
<br>
GitHub: https://github.com/SSAdhikari11
</p>
