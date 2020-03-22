import React from 'react';
import {geolocated} from "react-geolocated";
import Map from '../map/Map';
import {Form, Button} from "react-bootstrap";
import {
    LogoImgStyled,
    HeaderStyled,
    MapToggleButtonStyled,
    ContentContainerStyled
} from "./DashboardStyled"
import {FaMapMarkedAlt} from "react-icons/fa";
import MainContent from "../MainContent"


export class Dashboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            showMap: false,
            showZip: false,
        };
        this.toggleMap = this.toggleMap.bind(this);
        this.toggleZip = this.toggleZip.bind(this);
    };

    toggleMap() {
        this.setState({showMap: !this.state.showMap});
    };

    toggleZip() {
        this.setState({showZip: !this.state.showZip});
    };

    render() {
        const {isGeolocationAvailable, coords} = this.props;
        return (
            <>
                <HeaderStyled>
                    <LogoImgStyled src="img/logo_infocovid19.png" alt="Logo Info-Covid-19"/>
                    {this.state.showMap &&
                    <Form>
                        <Form.Control type="text" placeholder="PLZ tippen"/>
                        <Button type="submit" variant="primary" onClick={this.toggleZip}>Postleitzahl angeben</Button>
                    </Form>
                    }
                    <MapToggleButtonStyled type={'button'} mapIsOn={this.state.showMap} onClick={this.toggleMap}>
                        {!this.state.showMap?
                            <><span>Karte öffnen</span><FaMapMarkedAlt/></> :
                            <><span>Karte schließen</span><FaMapMarkedAlt/></>
                        }
                    </MapToggleButtonStyled>
                </HeaderStyled>
                <ContentContainerStyled>
                    {this.state.showMap ?
                        <Map
                            lat={(isGeolocationAvailable && coords) && coords.latitude}
                            lng={(isGeolocationAvailable && coords) && coords.longitude}
                        />
                        :
                        <MainContent/>
                    }
                </ContentContainerStyled>
            </>
        );
    }
}

export default geolocated({
    positionOptions: {
        enableHighAccuracy: false,
    },
    userDecisionTimeout: 5000,
})(Dashboard);