import React from 'react';
import { onMovieSelect } from '../../actions';

class MovieItem extends React.Component {

    constructor(props) {
        super(props);
        this.state = {spans: 0};
        this.imageRef = React.createRef();
    }

    componentDidMount() {
        this.imageRef.current.addEventListener('load', this.setSpans);
    }

    formatProviders(providers) {
        let providerString = "";
        providers.forEach(function (provider) {
            providerString += provider + ", ";
        })
        return providerString.slice(0, -2);
    }

    render() {
        const {title, thumbnail_url, imdb_rating, rt_rating} = this.props.movie;
        let providers = this.props.movie.providers;
        providers = this.formatProviders(providers);
        return (
            <tr className="movie-row">
                <td width="100px">
                    <img ref={this.imageRef} alt={title} src={thumbnail_url} className="middle aligned"/>
                </td>
                <td>
                    {title}                      
                </td>
                <td>
                    {imdb_rating}               
                </td>
                <td>
                    {rt_rating}
                </td>
                <td>
                    
                </td>
                <td>
                    {providers}
                </td>
            </tr>
        );
    }

}

export default MovieItem;