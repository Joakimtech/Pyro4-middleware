# Pyro4 Middleware  - Distributed Systems

## Overview
This project demonstrates middleware implementation using Pyro4 for distributed systems. It includes service discovery, multiple remote objects, error handling, asynchronous calls, persistence, and security.

## Activities Completed
1. Basic greeting service with Pyro4
2. Multiple remote services (Greeting, Calculator, Student)
3. Error handling and exception management
4. Asynchronous remote method calls
5. Object persistence with file storage
6. Security with authentication

## Installation

```bash
pip install Pyro4
```
## Running the Services
* Start the Name Server:

```bash
python -m Pyro4.naming
```
* Run any server:

```bash
python (server name).py
```
* Run corresponding client:

```bash
python (client name).py
```
## Files
* ```server.py / client.py ``` - Basic greeting service

* ```server_multiple.py / client_multiple.py``` - Multiple services

* ```server_error_handling.py / client_error_handling.py``` - Error handling

* ```server_async.py / client_async.py``` - Asynchronous calls

* ```counter_server.py / counter_client.py``` - Persistence

* ```secure_server.py / secure_client.py``` - Security

 ### outputs
 * #### client.py
   <img width="724" height="64" alt="image" src="https://github.com/user-attachments/assets/17e7dd30-9034-41ee-b250-8fa89f1815c8" />
 * 
 * #### counter_client.py
   <img width="684" height="162" alt="image" src="https://github.com/user-attachments/assets/df2429a0-de25-4089-9e5f-60e14a463c75" /> <br>
   <img width="699" height="211" alt="image" src="https://github.com/user-attachments/assets/f5490a89-df0f-4aab-b9df-89206698a80b" /> <br>
* #### secure_client.py
  <img width="682" height="349" alt="image" src="https://github.com/user-attachments/assets/a823e615-6e76-47af-9af9-c79885ae74e9" /> <br>


