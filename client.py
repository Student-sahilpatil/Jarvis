import google.generativeai as genai

genai.configure(api_key="AIzaSyCxGm_EFvP3GCPs2xS6E806ck2G_RHB_uw")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is coding")
print(response.text)

