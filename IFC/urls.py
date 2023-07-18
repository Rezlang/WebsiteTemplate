from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("documents", views.documents, name="documents"),
    path("chapters", views.ourChapters, name="chapters"),
    path("calendar", views.calendar, name="calendar"),
    path("constitution", views.constitution, name="constitution"),
    path("leadership", views.leadership, name="leadership"),

    
    path("Acacia", views.Acacia, name="Acacia"),
    path("AlphaEpsilonPi", views.AlphaEpsilonPi, name="AlphaEpsilonPi"),
    path("AlphaSigmaPhi", views.AlphaSigmaPhi, name="AlphaSigmaPhi"),
    path("AlphaChiRho", views.AlphaChiRho, name="AlphaChiRho"),
    path("ChiPhi", views.ChiPhi, name="ChiPhi"),
    path("DeltaKappaEpsilon", views.DeltaKappaEpsilon, name="DeltaKappaEpsilon"),
    path("DeltaPhi", views.DeltaPhi, name="DeltaPhi"),
    path("DeltaTauDelta", views.DeltaTauDelta, name="DeltaTauDelta"),
    path("LambdaChiAlpha", views.LambdaChiAlpha, name="LambdaChiAlpha"),
    path("PhiGammaDelta", views.PhiGammaDelta, name="PhiGammaDelta"),
    path("PhiKappaTheta", views.PhiKappaTheta, name="PhiKappaTheta"),
    path("PhiMuDelta", views.PhiMuDelta, name="PhiMuDelta"),
    path("PhiSigmaKappa", views.PhiSigmaKappa, name="PhiSigmaKappa"),
    path("PiKappaAlpha", views.PiKappaAlpha, name="PiKappaAlpha"),
    path("PiLambdaPhi", views.PiLambdaPhi, name="PiLambdaPhi"),
    path("PsiUpsilon", views.PsiUpsilon, name="PsiUpsilon"),
    path("SigmaAlphaEpsilon", views.SigmaAlphaEpsilon, name="SigmaAlphaEpsilon"),
    path("SigmaChi", views.SigmaChi, name="SigmaChi"),
    path("SigmaPhiEpsilon", views.SigmaPhiEpsilon, name="SigmaPhiEpsilon"),
    path("TauEpsilonPhi", views.TauEpsilonPhi, name="TauEpsilonPhi"),
    path("TauKappaEpsilon", views.TauKappaEpsilon, name="TauKappaEpsilon"),
    path("ThetaXi", views.ThetaXi, name="ThetaXi"),
    path("ZetaPsi", views.ZetaPsi, name="ZetaPsi"),
    
    
]
