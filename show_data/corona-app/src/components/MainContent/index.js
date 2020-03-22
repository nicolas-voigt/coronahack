import React from "react";
import {MainContentStyled, pStyled, LogoContainerStyled} from "./MainContentStyled";
import Profiles from "./Profiles";

const MainContent = () => {
    return (
        <>
            <MainContentStyled>
                <h3>Informationen zu Covid-19 – Einfach, lokal und offiziell</h3>
                <pStyled>
                    infocovid19.de ist die zentrale Anlaufstelle für aktuelle Meldungen staatlicher Stellen zur
                    Corona-Pandemie. Finden Sie hier offizielle Informationen, die auf Sie und Ihren Standort
                    zugeschnitten sind - einfach und lokal durch unsere Postleitzahlsuche.<br/>
                    Wie finde ich Informationen zu Covid-19?<br/>
                    Damit Sie Informationen zu Corona suchen können, klicken Sie einfach auf den Button “Karte öffnen”.
                    Anschließend können Sie durch die Angabe Ihrer Postleitzahl Ihren Standort angeben. Unsere Suche
                    zeigt Ihnen sodann die neuesten, offiziellen Meldungen der Ihnen nähsten staatlichen Behörde.<br/>
                    Woher weiß ich, dass die Informationen zu Corona vertrauenswürdig sind?<br/>
                    Das Verhängen von Schutzmaßnahmen, Ausgangsbeschränkungen und anderen Regelungen im Zusammenhang mit
                    der Corona-Pandemie ist Ländersache. Das bedeutet, dass es keine einheitliche bundesweite Regelungen
                    gibt. Deswegen stoßen viele Menschen bei ihrer Suche nach aktuellen Meldungen auf eine regelrechte
                    Flut an Informationen, die oftmals unsortiert und nicht vollständig ist.
                    <br/><br/>
                    Damit Sie nicht auch vor diesem Problem stehen, zeigt infocovid19.de Ihnen nur Informationen von
                    staatlichen, städtischen und kommunalen Websites an - verlässlich, offiziell und lokal.
                </pStyled>
                <Profiles/>
            </MainContentStyled>
            <LogoContainerStyled>
                <img src="img/Logo_Projekt_01.png" alt="logo"/>
                <img src="img/Logo_Projekt_02.png" alt="logo"/>
            </LogoContainerStyled>
        </>
    )
};

export default MainContent;