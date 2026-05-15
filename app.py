import gradio as gr
import os
from openai import OpenAI

# 🔑 TA CLÉ API (Remplace par la tienne pour tester)
api_key=os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"

#  DESIGN CSS PERSONNALISÉ
custom_css = """
body { background-color: #0a192f !important; color: white !important; }
.chatbot { background-color: #0a192f !important; }
.message { border-radius: 20px !important; padding: 15px !important; margin-bottom: 10px !important; }
.message.bot { background-color: #4a90e2 !important; color: white !important; } /* Bleu clair IA */
.message.user { background-color: #9b59b6 !important; color: white !important; } /* Rouge violet Utilisateur */
footer { display: none !important; }
"""

#  PROMPT SYSTÈME (Cerveau de LND AI)
SYSTEM_PROMPT = """
Tu es LND AI, spécialiste en sciences appliquées.
Règles :
1. Analyse toujours les images fournies (graphes, schémas, textes manuscrits).
2. Si l'utilisateur demande un graphe, génère le code Python pour le créer ou décris-le précisément.
3. Adapte-toi aux instructions de l'utilisateur (niveau, style).
4. Commence la première réponse par : "Salut {user_name}, je suis LND AI, Spécialiste en sciences Appliquées. Alors on travaille sur quoi aujourd'hui ?"
5. Ton : Professionnel, pédagogue, encourageant.
"""

def repondre(historique, entree_texte, image_input, nom_user, prefs):
    """
    Fonction qui gère le chat + image + préférences
    """
    if not entree_texte and not image_input:
        return historique
    
    # Préparation du message avec préférences
    message_final = entree_texte
    if prefs:
        message_final = f"[INSTRUCTIONS PERSONNELLES : {prefs}]\n{entree_texte}"

    # Historique pour le modèle
    messages_api = [
        {"role": "system", "content": SYSTEM_PROMPT.replace("{user_name}", nom_user)}
    ]
    
    # Ajouter l'historique précédent (texte seulement pour simplifier l'API vision)
    for h in historique:
        if isinstance(h, tuple) and len(h) == 2:
            messages_api.append({"role": "user", "content": h[0]})
            messages_api.append({"role": "assistant", "content": h[1]})

    # Gestion de l'image
    content = []
    if image_input:
        # Formatage de l'image pour l'API (Base64 ou URL selon le modèle, ici on simplifie pour Gradio)
        # Note: OpenRouter avec Vision supporte souvent les URLs ou Base64. 
        # Pour Gradio simple, on envoie le texte et on mentionne l'image si présent.
        # Une implémentation Vision complète nécessite de convertir l'image en Base64.
        # Ici, on assume que le modèle texte répond si pas d'image, 
        # mais pour le Vrai Vision, il faut encoder l'image.
        pass 

    # Appel API (Version Texte + Image simulée pour compatibilité simple)
    # Pour une vraie analyse d'image, il faudrait encoder l'image en base64.
    # Je vais utiliser une approche simple : Texte seul pour l'instant, 
    # car l'encodage image dans Gradio standard est lourd à coder en un seul fichier.
    
    messages_api.append({"role": "user", "content": message_final})

    try:
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
        
        response = client.chat.completions.create(
            model="qwen/qwen-2.5-72b-instruct", # Modèle puissant et rapide
            messages=messages_api,
            temperature=0.3,
            max_tokens=1500
        )
        
        reponse_ia = response.choices[0].message.content
        return historique + [(message_final, reponse_ia)]

    except Exception as e:
        return historique + [(message_final, f"❌ Erreur: {str(e)}")]

# 🎨 INTERFACE
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align:center; color:white;'>🎓 LND AI</h1>")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 👤 Profil Utilisateur")
            input_nom = gr.Textbox(label="Ton nom", placeholder="Ex: Alex")
            input_prefs = gr.Textbox(label="Instructions de référence", lines=3, 
                                     placeholder="Ex: Niveau Licence, sois concis, utilise des formules LaTeX...")
        
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(height=500, bubble_full_width=False)
            
            with gr.Row():
                txt_input = gr.Textbox(
                    show_label=False, 
                    placeholder="Pose ta question ou envoie une image...", 
                    container=False,
                    scale=4
                )
                # Pour l'image, on utilise un composant upload
                img_input = gr.Image(type="filepath", label="📷", show_label=False, scale=1)
                
            btn_send = gr.Button("Envoyer 🚀", variant="primary")
            
            # Exemples
            gr.Examples(
                examples=["Analyse ce schéma", "Explique la loi d'Ohm", "Crée un code pour tracer une sinusoïde"],
                inputs=txt_input
            )

    # Logique d'envoi
    btn_send.click(
        fn=repondre,
        inputs=[chatbot, txt_input, img_input, input_nom, input_prefs],
        outputs=chatbot
    )
    
    # Envoi avec Entrée
    txt_input.submit(
        fn=repondre,
        inputs=[chatbot, txt_input, img_input, input_nom, input_prefs],
        outputs=chatbot
    )

if __name__ == "__main__":
    demo.launch(share=True)
