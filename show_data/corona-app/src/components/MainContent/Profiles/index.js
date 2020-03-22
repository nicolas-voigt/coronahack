import React from "react";
import {ProfilesData} from "./ProfilesData";
import {ProfilesContainerStyled} from "./ProfileStyled";
import Profile from "./Profile";

const Profiles = () => {
    return <ProfilesContainerStyled>
        {ProfilesData && ProfilesData.map((item, index) => (
            <Profile
                key={index}
                name={item.name}
                role={item.role}
                github={item.github}
                linkedin={item.linkedin}
                twitter={item.twitter}
                website={item.website}
                pic={item.pic}
            />
        ))}
    </ProfilesContainerStyled>
};

export default Profiles;
