![image](https://github.com/flaviomicheletti/python-aws/assets/1257048/258389b4-6840-4083-8641-77782e299a5e)

# Python on AWS

This repository contains a collection of Python scripts that demonstrate how 
to interact with various AWS services using the Boto3 library. These scripts 
can be used as a starting point for testing and experimenting with different 
AWS services and their functionalities.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Config](#config)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using the scripts in this repository, ensure that you have the following prerequisites:

- Python 3.x installed on your machine.
- An AWS account with the necessary permissions to access the AWS services you intend to test.
- Boto3 library installed. You can install it by running the following command:

  ```
  pip install boto3
  ```

- AWS credentials set up on your local machine. You can configure your AWS 
credentials by either setting environment variables or using the AWS CLI. 
Refer to the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) 
for detailed instructions.

## Installation

To use the scripts in this repository, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/python-aws.git
   ```

2. Install the required dependencies:

   ```
   python3 -m venv .venv && . .venv/bin/activate

   //Show the envs:
   pyenv virtualenvs

   // Choose one
   pyenv activate py311

   pip install -r requirements.txt
   ```

## Usage

The scripts in this repository are organized into directories based on the 
AWS service they interact with. Each script is self-contained and can be 
executed independently. 

1. Navigate to the directory of the AWS service you want to test:

   ```
   cd service-name
   ```

2. Review the script files in the directory and choose the one that suits your
   testing requirements.

3. Open the chosen script file and configure any necessary parameters, such as 
   region, credentials, or input data.

4. Run the script using Python:

   ```
   python script-name.py
   ```

5. Observe the output and check the AWS service console to verify the actions performed by the script.

## Config


```python
# config.py
access = ''
secret = ''

type = 'sqs'
region = 'us-east-1'
queue_url = 'https://sqs.us-east-1.amazonaws.com/659014245856/myqueue'
```

## Contributing

Contributions to this repository are welcome. If you would like to contribute, 
please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request describing your changes.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to modify 
and use the code for your own purposes.


