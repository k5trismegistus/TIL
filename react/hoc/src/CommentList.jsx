import React from 'react';
import {withSubscription} from './withSubscription';

class CommentList extends React.Component {
  render() {
    return (
      <div>
        {this.state.comments.map((comment) => (
          <Comment comment={comment} key={comment.id} />
        ))}
      </div>
    );
  }
}

const getComments = (Datasource, props) => (DataSource.getComments());

export default const wrappedCommentList = withSubscription(CommentList, getComments);