import React, { Component } from "react";

import './App.css';
export default class SignUp extends Component {
  render() {
      return (
          <form>
              <h3>Ninja Boootcamp Todo List</h3>

              <div className="form-group">
                  <label>Name</label>
                  <input type="text" className="form-control" placeholder="First name" />
              </div>

              <div className="form-group">
                  <label>Number</label>
                  <input type="text" className="form-control" placeholder="Last name" />
              </div>

              <div className="form-group">
                  <label>Github Link</label>
                  <input type="email" className="form-control" placeholder="Enter email" />
              </div>

              <div className="form-group">
                  <label>Berif Description</label>
                  <input type="password" className="form-control" placeholder="Enter password" />
              </div>

              <button type="submit" className="btn btn-primary btn-block">Submit</button>
          </form>
      );
  }
}