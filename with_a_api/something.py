import os
from typing import Optional
from openai import OpenAI, APIError


def create_hf_client() -> OpenAI:
    """Create and return an OpenAI client configured for HuggingFace."""
    api_key = os.environ.get("HF_TOKEN")
    if not api_key:
        raise ValueError("HF_TOKEN environment variable not set")
    
    return OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=api_key,
    )


def query_model(
    client: OpenAI,
    message: str,
    model: str = "meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
) -> str:
    """
    Query the HuggingFace API with a message.
    
    Args:
        client: OpenAI client configured for HuggingFace
        message: The user message to send
        model: The model to use (default: Llama 3.1 8B)
        temperature: Sampling temperature (0-1)
        max_tokens: Maximum tokens in response
    
    Returns:
        The assistant's response text
    
    Raises:
        APIError: If the API request fails
    """
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return completion.choices[0].message.content
    except APIError as e:
        print(f"API Error: {e}")
        raise


if __name__ == "__main__":
    try:
        client = create_hf_client()
        response = query_model(client, "What is the capital of France?")
        print(f"Response: {response}")
    except (ValueError, APIError) as e:
        print(f"Error: {e}")