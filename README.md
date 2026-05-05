# Network Security Experiments

A collection of Python-based experiments implementing various cryptographic algorithms and digital signatures for network security.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Virtual Environment (recommended)

### Setup
1. **Clone the repository** (or navigate to the folder).
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Experiments Overview

### 1. Alphabet Position Encryption
- **File**: `exp1_alphabet_position.py`
- **Theory**: Converts letters to their numeric positions in the alphabet. Uppercase letters become positive numbers, while lowercase letters become negative numbers.
- **Run**: `python exp1_alphabet_position.py`

### 2. Caesar & Substitution Ciphers
- **File**: `exp2_ciphers.py`
- **Theory**: 
  - **Caesar Cipher**: A substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet.
  - **Substitution Cipher**: Replaces each letter with another letter based on a fixed key (permutation of the alphabet).
- **Run**: `python exp2_ciphers.py`

### 3. Digital Signature using RSA
- **File**: `exp3_rsa_signature.py`
- **Theory**: Demonstrates how a digital signature is generated using a private key and verified using a public key based on the RSA algorithm principles.
- **Run**: `python exp3_rsa_signature.py`

### 4. Symmetric vs Asymmetric Cryptography
- **File**: `exp5_symmetric_asymmetric.py`
- **Theory**: Compares the two main types of cryptography:
  - **Symmetric**: Same key for encryption and decryption (e.g., Caesar).
  - **Asymmetric**: Different keys for encryption (Public) and decryption (Private) (e.g., RSA).
- **Run**: `python exp5_symmetric_asymmetric.py`

### 5. Data Encryption Standard (DES)
- **File**: `exp6_des.py`
- **Theory**: Implementation of the DES symmetric-key block cipher using an 8-byte key.
- **Run**: `python exp6_des.py`

### 6. Advanced Encryption Standard (AES)
- **File**: `exp7_aes.py`
- **Theory**: Implementation of the AES symmetric-key block cipher, which is more secure and efficient than DES. Uses a 16-byte key (128-bit).
- **Run**: `python exp7_aes.py`

---

## 🛠 Dependencies
- `pycryptodome`: Used for DES and AES implementations.

---

## 📝 License
This project is for educational purposes.
