import React from react;
import {withSubscription} from './withSubscription';

class BlogPost extends React.Component {
  render() {
    return <TextBlock text={this.state.blogPost} />;
  }
}

const getBlogPost = (DataSource, props) => (DataSource.getBlogPost(props.id))

export default wrappedBlogPost = withSubscription(BlogPost, getBlogPost);