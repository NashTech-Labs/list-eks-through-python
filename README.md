# EKS Cluster Listing Script

This script lists all **active** Amazon EKS (Elastic Kubernetes Service) clusters in a specified AWS region using Boto3.

## Prerequisites

Before running this script, ensure the following:

1. **Python 3.x** is installed. Download it from [python.org](https://www.python.org/downloads/).
2. **Boto3** is installed (AWS SDK for Python).
3. You have **AWS IAM credentials** (Access Key and Secret Access Key) with permissions to list and describe EKS clusters.

## Installation

### 1. Clone the repository or download the script

```bash
git clone <repository-url>
cd <script-directory>
```

### 2. Install required Python packages

Ensure you have Boto3 installed. If not, install it using `pip`:

```bash
pip install boto3
```

## AWS Setup

Make sure you have your **AWS Access Key**, **Secret Access Key**, and the **Region** where your EKS clusters are hosted. You can retrieve these from the AWS Console.

## Usage

1. Open the script and replace the placeholders with your AWS credentials and region:

   ```python
   aws_access_key_id=<access_key>
   aws_secret_access_key=<secret_access>
   region_name='<region>'```

2. Run the script:

```python
python list_eks.py```
