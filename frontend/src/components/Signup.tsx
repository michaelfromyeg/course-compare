import React from 'react';
import { Formik, Field, Form, FormikHelpers } from 'formik';

interface LoginFields {
    firstName: string;
    lastName: string;
    email: string;
    password: string;
}

const Signup = () =>  {
    return (
        <div className="signup">
            <h1>Sign Up Form</h1>
            <Formik
                initialValues={{ firstName: '', lastName: '', email: '', password: '' }}
                validate={values => {
                    const errors = {
                        firstName: '',
                        lastName: '',
                        email: ''
                    };
                    if (!values.firstName) {
                        errors.firstName = 'Required';
                    }
                    if (!values.lastName) {
                        errors.lastName = 'Required';
                    }
                    if (!values.email) {
                        errors.email = 'Required';
                    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
                        errors.email = 'Invalid email address';
                    }
                    return errors;
                }}
                onSubmit={(
                    values: LoginFields, 
                    { setSubmitting }: FormikHelpers<LoginFields>
                ) => {
                    setTimeout(() => {
                        alert(JSON.stringify(values, null, 2));
                        setSubmitting(false);
                    }, 400);
                }}
                >
                    {({
                        values,
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        handleSubmit,
                        isSubmitting
                    }) => (
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="firstName">firstName</label>
                            <input
                                type="text"
                                name="firstName"
                                id="firstName"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.firstName}
                            />
                            <br />
                            {errors.firstName && touched.firstName && errors.firstName}
                            <br />
                            <label htmlFor="lastName">Last Name</label>
                            <input
                                type="text"
                                name="lastName"
                                id="lastName"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.lastName}
                            />
                            <br />
                            {errors.lastName && touched.lastName && errors.lastName}
                            <br />
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                name="email"
                                id="email"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.email}
                            />
                            <br />
                            {errors.email && touched.email && errors.email}
                            <br />
                            <label htmlFor="password">Password</label>
                            <input 
                                type="password"
                                name="password"
                                id="password"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.password}
                            />
                            <br />
                            {errors.password && touched.password && errors.password}
                            <br />
                            <button type="submit" disabled={isSubmitting}>
                                Sign up
                            </button>
                        </form>
                    )}
            </Formik>
        </div>
    )
}

export default Signup