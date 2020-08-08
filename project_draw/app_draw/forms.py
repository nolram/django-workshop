from django import forms


class PrizeDrawForm(forms.Form):
    draw_name = forms.CharField(
        label="Nome do Sorteio",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    participants = forms.CharField(
        label="Participantes",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 20})
    )
    quantity = forms.IntegerField(
        label="Quantidade",
        widget=forms.NumberInput(attrs={"class": "form-control"}), initial=1, min_value=1
    )
