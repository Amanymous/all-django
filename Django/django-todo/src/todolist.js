import React from 'react';


const todo = ( props ) => {
    return (
        <form>
        <label>
          Name:
          <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
        <label>
          Number:
          <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
        <label>
          Github Link:
          <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
        <label>
          Brief Description:
          <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
      </form>
     
    )
    
};

export default todo;