import React from "react";
import {
    NameStyled,
    RoleStyled,
    LinkStyled,
    PicContainerStyled, ProfileStyled,
    ContentContainerStyled,
    LinkContainer
} from './ProfileStyled';
import {FaLinkedin, FaTwitterSquare, FaGithubSquare, FaLink} from 'react-icons/fa';

const Profile = (props) => {
    const {name, role, github, linkedin, twitter, website, pic} = props;
    return <>
        <ProfileStyled>
            <PicContainerStyled>
                {pic && <img src={`img/team/${pic}`} alt="Profilbild"/>}
            </PicContainerStyled>
            <ContentContainerStyled>
                {name && <NameStyled>{name}</NameStyled>}
                {role && <RoleStyled>{role}</RoleStyled>}
                <LinkContainer>
                    {github && <LinkStyled href={github} target="_blank" title="github"><FaGithubSquare/></LinkStyled>}
                    {linkedin && <LinkStyled href={linkedin} target="_blank" title="linkedin"><FaLinkedin/></LinkStyled>}
                    {twitter && <LinkStyled href={twitter} target="_blank" title="twitter"><FaTwitterSquare/></LinkStyled>}
                    {website && <LinkStyled href={website} target="_blank" title="website"><FaLink/></LinkStyled>}
                </LinkContainer>
            </ContentContainerStyled>
        </ProfileStyled>
    </>
};

export default Profile;
