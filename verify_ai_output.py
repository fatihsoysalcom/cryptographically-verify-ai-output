import hashlib
import json

def generate_ai_output(prompt):
    """Simulates generating AI output."""
    # In a real scenario, this would be a call to an LLM API.
    # For demonstration, we'll use a fixed response.
    response_text = f"Based on your prompt '{prompt}', here is some information."
    return {
        "prompt": prompt,
        "generated_text": response_text,
        "metadata": {
            "model": "simulated_llm_v1",
            "timestamp": "2023-10-27T10:00:00Z"
        }
    }

def create_proof(ai_output):
    """Creates a cryptographic proof (hash) of the AI output."""
    # Convert the output to a deterministic JSON string to ensure consistent hashing.
    output_string = json.dumps(ai_output, sort_keys=True, separators=(',', ':'))
    # Use SHA-256 for hashing.
    proof = hashlib.sha256(output_string.encode('utf-8')).hexdigest()
    return proof

def verify_proof(original_output, provided_proof):
    """Verifies if the provided proof matches the hash of the original output."""
    # Re-generate the proof from the original output.
    recalculated_proof = create_proof(original_output)
    # Compare the provided proof with the recalculated proof.
    return provided_proof == recalculated_proof

if __name__ == "__main__":
    # 1. Simulate receiving AI output
    user_prompt = "What is the capital of France?"
    ai_response_data = generate_ai_output(user_prompt)
    print("--- AI Output ---")
    print(json.dumps(ai_response_data, indent=2))
    print("\n")

    # 2. Create a cryptographic proof of this output
    # In a real system, the AI provider would generate and return this proof.
    generated_proof = create_proof(ai_response_data)
    print(f"--- Generated Proof (Hash) ---")
    print(generated_proof)
    print("\n")

    # 3. Simulate verification by a third party or the user
    # The verifier needs the original AI output and the proof.
    print("--- Verification ---")
    is_valid = verify_proof(ai_response_data, generated_proof)
    print(f"Is the AI output authentic? {is_valid}")

    # Example of tampered data (simulating a malicious change)
    tampered_output = ai_response_data.copy()
    tampered_output["generated_text"] = "The capital of France is actually Berlin."
    print("\n--- Verification with Tampered Data ---")
    is_valid_tampered = verify_proof(tampered_output, generated_proof)
    print(f"Is the tampered AI output authentic? {is_valid_tampered}")
