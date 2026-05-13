import gradio as gr

# 🎓 Prompt système : LND AI détecte automatiquement le contexte
SYSTEM_PROMPT = """Tu es LND AI, un tuteur expert multi-disciplines.

Domaines : Maths, Physique, Chimie, Biologie, Informatique & IT.

Règles :
1. Réponds en français, ton clair et encourageant.
2. Détecte automatiquement la matière et le niveau.
3. Décompose en étapes pour les problèmes complexes.
4. Montre la démarche avant le résultat.
5. Utilise LaTeX pour les formules : $E=mc^2$
6. Si flou, pose une question pour préciser.
7. Termine par : "Veux-tu un exercice ou que je détaille un point ?"
"""

def repondre(question, history=None):
    """Fonction de chat simple"""
    if not question or not question.strip():
        return "👋 Bonjour ! Pose ta question en sciences ou informatique. Je suis là pour t'aider !"
    
    # 🔄 Réponse de test (on connectera l'IA après)
    return f"""✅ **LND AI a reçu :** "{question}"

⏳ *Mode démo : la vraie IA sera connectée à la prochaine étape.*

💡 **Exemples de questions :**
- "Explique la loi d'Ohm"
- "Dérivée de x² + 3x ?"
- "Comment fonctionne une boucle for en Python ?"
- "Qu'est-ce qu'une réaction redox ?"

🎯 Pose ta vraie question, je suis prêt !"""

# 🎨 Interface chatbot simple et compatible
with gr.Blocks(title="🎓 LND AI", as demo:
    gr.Markdown("# 🎓 LND AI\n*Tuteur intelligent en sciences et technologies*")
    gr.Markdown("Pose ta question. Je détecte automatiquement le contexte. 🚀")
    
    # Interface simple : 1 input texte, 1 output texte
    with gr.Row():
        question = gr.Textbox(
            label="Ta question",
            placeholder="Ex: Explique la 2ème loi de Newton...",
            lines=2
        )
        sortie = gr.Textbox(label="Réponse de LND AI", lines=10)
    
    btn = gr.Button("🚀 Envoyer", variant="primary")
    btn.click(fn=repondre, inputs=question, outputs=sortie)
    
    # Exemples cliquables
    gr.Examples(
        examples=[
            "Explique la loi d'Ohm avec un exemple",
            "Comment calculer une dérivée ?",
            "Qu'est-ce qu'une boucle for en Python ?",
            "Explique le théorème de Pythagore"
        ],
        inputs=question
    )
    
    gr.Markdown("---\n*Projet LND AI par @lnkstructures — Licence MIT*")

# Lancement avec thème corrigé
if __name__ == "__main__":
    demo.launch(share=True)
