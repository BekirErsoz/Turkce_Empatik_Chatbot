        from transformers import pipeline
        from loguru import logger

        class EmpathicResponder:
            def __init__(self):
                logger.info("Loading BLOOMZ model for response...")
                # BLOOMZ-560M supports Turkish; small enough for CPU
                self.pipe = pipeline(
                    "text-generation",
                    model="bigscience/bloomz-560m",
                    device=-1,
                    max_new_tokens=100
                )
                logger.info("Response model loaded.")

            def __call__(self, user_text: str, sentiment_label: str):
                prompt = (
                    "Aşağıdaki konuşmada bir kullanıcı ve empatik bir asistan var.
"
                    f"Kullanıcı ({sentiment_label}): {user_text}
"
                    "Asistan (empatik ve destekleyici, gerekirse kısa bir öneri sunar):"
                )
                generated = self.pipe(prompt, do_sample=True, top_p=0.9, temperature=0.7)[0]["generated_text"]
                reply = generated.split("Asistan")[-1].replace(":", "").strip()
                return reply
