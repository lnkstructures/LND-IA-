import os
import gradio as gr

# 🎓 Prompt système : LND AI détecte automatiquement le contexte
SYSTEM_PROMPT = """Tu es LND AI, un tuteur expert multi-disciplines.

Domaines d'expertise :
- 📐 Mathématiques (algèbre, analyse, probabilités, statistiques, géométrie, complément mathématiques, calcule scientifique, mathématiques informatique)
- 🔬 Physique (mécanique, électromagnétisme, thermodynamique, optique, électricité , quantique, nano technologie, )
- ⚗️ Chimie (réactions, stoichiométrie, organique, inorganique, structure de la matière, énergie)
- 🧬 Biologie (cellulaire, génétique, physiologie, écosystèmes)
- 💻 Informatique & Technologies IT (algorithmes, programmation, réseaux, cybersécurité, IA, développement web, architecture des ordinateurs)

Règles pédagogiques :
1. Réponds TOUJOURS en français, avec un ton clair, patient et encourageant.
2. Détecte automatiquement la matière et le niveau à partir de la question.
3. Décompose en étapes numérotées pour les problèmes complexes.
4. Pour les calculs : montre la démarche avant le résultat.
5. Utilise le format LaTeX pour les formules : $E=mc^2$ ou $$...$$
6. Si la question est floue, pose une question pour préciser.
7. Adapte automatiquement ton niveau de détail (débutant → avancé).
8. Termine par : "Veux-tu un exercice d'application ou que je détaille un point ?"

Structure de réponse type :
🎯 **Concept clé** : [explication courte]
📝 **Développement** : [étapes détaillées]
💡 **Astuce** : [conseil pratique]
✅ **Vérification** : [si applicable]
"""

def repondre(question, history=None):
    """Fonction de chat : reçoit la question → génère la réponse"""
    if not question or question.strip() == "":
        return " Bonjour ! Pose-moi ta question en maths, physique, chimie, biologie ou informatique. Je suis là pour t'aider !"
    
    # 🔄 Pour l'instant : réponse de test (on connectera l'IA après)
    reponse = f"""✅ **LND AI a reçu ta question !** (mode démo)

📝 **Question** : {question}

⏳ *Prochaine étape : je vais connecter un vrai modèle IA gratuit pour générer des réponses intelligentes et précises.*

💡 **En attendant**, voici ce que LND AI fera :
- Détecter automatiquement la matière (maths, physique, chimie, biologie, informatique)
- Identifier ton niveau à partir de ta question
- T'expliquer pas à pas avec des formules bien formatées
- Te proposer des exercices d'application

🧪 **Test rapide** : Essaie une question comme :
- "Explique la loi d'Ohm"
- "Comment calculer une dérivée ?"
- "Qu'est-ce qu'une boucle for en Python ?"
"""
    return reponse

# 🎨 Interface chatbot ultra-simple
with gr.Blocks(title="🎓 LND AI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎓 LND AI\n*Tuteur intelligent en sciences et technologies*")
    gr.Markdown("Pose ta question en **maths, physique, chimie, biologie ou informatique**. Je détecte automatiquement le contexte et t'explique pas à pas. 🚀")
    
    chatbot = gr.ChatInterface(
        fn=repondre,
        placeholder="Ex: Explique la deuxième loi de Newton ou comment fonctionne une fonction en Python...",
        examples=[
            "Explique la loi d'Ohm avec un exemple concret",
            "Comment calculer la dérivée de x² + 3x ?",
            "Qu'est-ce qu'une réaction d'oxydoréduction ?",
            "Explique le théorème de Pythagore",
            "Comment fonctionne une boucle for en Python ?"
        ],
        title="",
        description=""
    )
    
    gr.Markdown("---\n*Projet LND AI par @lnkstructures — Code open-source sous licence MIT*")

# Lancement
if __name__ == "__main__":
    demo.launch(share=True)
