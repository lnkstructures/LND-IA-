import os
import gradio as gr

# 🎓 Prompt système : le "cerveau pédagogique" de LND AI
SYSTEM_PROMPT = """Tu es LND AI, un tuteur expert en :
- Mathématiques (algèbre, analyse, probabilités)
- Physique (mécanique, électromagnétisme, thermodynamique, quantique) ⭐ PRIORITAIRE
- Chimie (réactions, stoichiométrie, organique)
- Biologie (cellulaire, génétique, écosystèmes)
- Informatique & Technologies IT (algorithmes, code, réseaux, cybersécurité) ⭐ PRIORITAIRE

Règles pédagogiques :
1. Réponds TOUJOURS en français, avec un ton clair et encourageant.
2. Décompose chaque réponse en étapes numérotées.
3. Pour les calculs : montre la démarche avant le résultat.
4. Pour les formules : utilise le format LaTeX entre $...$ (ex: $E=mc^2$).
5. Si la question est floue, pose une question pour préciser avant de répondre.
6. Adapte ton niveau : débutant → intermédiaire → avancé selon la demande.
7. Termine par : "Veux-tu un exercice d'application ou que je détaille un point ?"

Exemple de réponse type :
[Étape 1] Rappel du concept...
[Étape 2] Application à ton cas...
[Étape 3] Résultat + vérification...
💡 Astuce : ...
"""

def repondre(question, matiere="Physique", niveau="Intermédiaire"):
    """Fonction principale : reçoit la question → génère la réponse"""
    # Construction du prompt complet
    prompt = f"{SYSTEM_PROMPT}\n\n[CONTEXTE] Matière: {matiere} | Niveau: {niveau}\n[QUESTION] {question}\n[LND AI]"
    
    # 🔄 Ici, on simulera la réponse pour l'instant (on connectera l'IA après)
    # On retourne un message de test pour valider que l'interface fonctionne
    return f"""✅ **LND AI est prête !** (mode démo)

📝 Ta question : *{question}*  
🔬 Matière : {matiere} | 🎓 Niveau : {niveau}

⏳ *Prochaine étape : on connectera un vrai modèle IA pour générer des réponses intelligentes.*

💡 En attendant, teste l'interface avec différentes questions !"""

# 🎨 Interface utilisateur avec Gradio
with gr.Blocks(title="🎓 LND AI - Tuteur Scientifique", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎓 LND AI\n*Tuteur intelligent en Maths, Physique, Chimie, Biologie & Informatique*")
    
    with gr.Row():
        with gr.Column():
            question = gr.Textbox(label="Ta question", placeholder="Ex: Explique la loi d'Ohm ou comment fonctionne une boucle for en Python...", lines=3)
            matiere = gr.Dropdown(
                choices=["Physique", "Informatique", "Mathématiques", "Chimie", "Biologie"],
                value="Physique",
                label="Matière"
            )
            niveau = gr.Dropdown(
                choices=["Débutant", "Intermédiaire", "Avancé"],
                value="Intermédiaire",
                label="Niveau"
            )
            btn = gr.Button("🚀 Obtenir l'explication", variant="primary")
        
        with gr.Column():
            sortie = gr.Markdown(label="Réponse de LND AI")
    
    btn.click(fn=repondre, inputs=[question, matiere, niveau], outputs=sortie)
    
    gr.Markdown("---\n*Projet LND AI par @lnkstructures — Code open-source sous licence MIT*")

# Lancement de l'application
if __name__ == "__main__":
    demo.launch(share=True)
