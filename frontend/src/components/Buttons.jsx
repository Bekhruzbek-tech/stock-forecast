import React from 'react'
import { Link } from 'react-router-dom'

const Button = ({
  text,
  url,
  variant = 'primary',
  size = 'md',
  extraClass = ''
}) => {
  return (
    <Link
      to={url}
      className={`btn btn-${variant} btn-${size} ${extraClass}`}
    >
      {text}
    </Link>
  )
}

export default Button